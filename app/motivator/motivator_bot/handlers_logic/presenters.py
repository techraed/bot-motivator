from typing import Union, List
from abc import ABCMeta, abstractmethod

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ConversationHandler

from app.motivator.users.bot_users import NewBotUser, KnownBotUser
from app.motivator.motivator_bot import constants


class TelegramPresenter(metaclass=ABCMeta):
    def __init__(self, update: Update, context: CallbackContext = None):
        self._update = update
        self._context = context

    def present_response(self):
        self._update.message.reply_text(
            text=self.text,
            reply_markup=self.reply_keyboard
        )

    @abstractmethod
    def reply_keyboard(self) -> Union[ReplyKeyboardRemove, ReplyKeyboardMarkup]:
        raise NotImplementedError

    @abstractmethod
    def text(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def next_state(self) -> int:
        raise NotImplementedError


class StartPresenter(TelegramPresenter):
    def __init__(self, update: Update, context: CallbackContext):
        super().__init__(update, context)
        self._user_answer_choices: List[List[str]] = [constants.READY_TO_START_ANSWERS]
        self._bot_user: Union[NewBotUser, KnownBotUser] = self._context.user_data['bot_user_class']

    @property
    def text(self) -> str:
        if self._bot_user.can_start():
            return self._get_typed_user_greet_message()
        return constants.CANT_START_GREETING

    def _get_typed_user_greet_message(self) -> str:
        """todo potentially excessive. what if there are multiple user types? The only solution I saw was storing greet
            message in User class, but it's does not suit logic
        """
        if isinstance(self._bot_user, NewBotUser):
            return constants.NEW_USER_GREETING
        return constants.KNOWN_USER_GREETING

    @property
    def reply_keyboard(self) -> Union[ReplyKeyboardRemove, ReplyKeyboardMarkup]:
        if self._bot_user.can_start():
            return ReplyKeyboardMarkup(self._user_answer_choices, one_time_keyboard=True)
        return ReplyKeyboardRemove()

    @property
    def next_state(self):
        if self._bot_user.can_start():
            return constants.REACT_START_CHOICE
        return ConversationHandler.END


def cancellation_goodbye(update: Update):
    reply_keyboard = ReplyKeyboardRemove()
    reply_text: str = constants.SAY_GOODBYE
    update.message.reply_text(
        text=reply_text,
        reply_markup=reply_keyboard
    )


def show_habits(update: Update):
    habits: List[List[str]] = [constants.HABITS_CHOICE_ANSWERS]
    reply_keyboard = ReplyKeyboardMarkup(habits, one_time_keyboard=True)
    reply_text: str = constants.CHOOSE_HABITS
    update.message.reply_text(
        text=reply_text,
        reply_markup=reply_keyboard
    )


def confirm_choice(update: Update):
    reply_keyboard = ReplyKeyboardRemove()
    reply_text: str = constants.CONFIRM_CHOICE
    update.message.reply_text(
        text=reply_text,
        reply_markup=reply_keyboard
    )
