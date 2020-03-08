from typing import Union, List
from abc import ABCMeta, abstractmethod

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ConversationHandler

from app.motivator.users.bot_users import NewBotUser, KnownBotUser
from app.motivator import constants
from app.app_data.user_data_manager import user_data_manager


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
        self._bot_user: Union[NewBotUser, KnownBotUser] = self._context.user_data['bot_user_instance']

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


class ShowHabitsPresenter(TelegramPresenter):
    def __init__(self, update: Update, context: CallbackContext):
        super().__init__(update, context)
        self._user_start_response: str = self._context.user_data['user_start_response']
        self._bot_user: Union[NewBotUser, KnownBotUser] = self._context.user_data['bot_user_instance']

    @property
    def text(self) -> str:
        if self._is_not_affirmative_choice():
            return constants.SAY_GOODBYE
        return constants.CHOOSE_HABITS

    @property
    def reply_keyboard(self) -> Union[ReplyKeyboardRemove, ReplyKeyboardMarkup]:
        if self._is_not_affirmative_choice():
            return ReplyKeyboardRemove()

        available_habits: List[List[str]] = [self._bot_user.get_available_habits()]
        return ReplyKeyboardMarkup(available_habits, one_time_keyboard=True)

    def _is_not_affirmative_choice(self):
        return self._user_start_response == constants.NO

    @property
    def next_state(self) -> int:
        if self._is_not_affirmative_choice():
            return ConversationHandler.END
        return constants.REACT_HABIT_CHOICE


class ChoiceConfirmPresenter(TelegramPresenter):
    def __init__(self, update: Update):
        super().__init__(update)

    @property
    def text(self) -> str:
        return constants.CONFIRM_CHOICE

    @property
    def reply_keyboard(self) -> Union[ReplyKeyboardRemove, ReplyKeyboardMarkup]:
        return ReplyKeyboardRemove()

    @property
    def next_state(self) -> int:
        return ConversationHandler.END


class DeletePresenter(TelegramPresenter):
    def __init__(self, update: Update, context: CallbackContext):
        super().__init__(update, context)
        self._user_answer_choices: List[List[str]] = [constants.READY_TO_DELETE_ANSWERS]
        self._bot_user: Union[NewBotUser, KnownBotUser] = self._context.user_data['bot_user_instance']
        self.user_id: int = self._update.message.chat.id
        self.user_data: dict = user_data_manager.get_user_data(self.user_id)

    def is_length(self):
        return len(self.user_data['habits']) > 0

    @property
    def text(self) -> str:
        if self.is_length():
            return constants.DELETE_GREETING
        return constants.CANT_DELETE

    @property
    def reply_keyboard(self) -> Union[ReplyKeyboardRemove, ReplyKeyboardMarkup]:
        if self.is_length():
            return ReplyKeyboardMarkup(self._user_answer_choices, one_time_keyboard=True)
        return ReplyKeyboardRemove()

    @property
    def next_state(self):
        if self.is_length():
            return constants.REACT_DELETE_CHOICE
        return ConversationHandler.END


class ShowUserHabitsPresenter(TelegramPresenter):
    def __init__(self, update: Update, context: CallbackContext):
        super().__init__(update, context)
        self._user_delete_response: str = self._context.user_data['user_delete_response']
        self._bot_user: Union[NewBotUser, KnownBotUser] = self._context.user_data['bot_user_instance']
        self.user_id: int = self._update.message.chat.id
        self.user_data: dict = user_data_manager.get_user_data(self.user_id)

    @property
    def text(self) -> str:
        if self._is_not_affirmative_choice():
            return constants.DONT_DELETE
        return constants.CHOOSE_HABITS_TO_DELETE

    @property
    def reply_keyboard(self) -> Union[ReplyKeyboardRemove, ReplyKeyboardMarkup]:
        if self._is_not_affirmative_choice():
            return ReplyKeyboardRemove()
        user_habits_list1 = []
        for i in self.user_data['habits']:
            user_habits_list = [(i['habit_name'])]
            user_habits_list1.append(user_habits_list)
        return ReplyKeyboardMarkup(user_habits_list1, one_time_keyboard=True)

    def _is_not_affirmative_choice(self):
        return self._user_delete_response == constants.NO

    @property
    def next_state(self) -> int:
        if self._is_not_affirmative_choice():
            return ConversationHandler.END
        return constants.REACT_SHOW_CHOICE


class DeleteConfirmPresenter(TelegramPresenter):
    def __init__(self, update: Update):
        super().__init__(update)

    @property
    def text(self) -> str:
        return constants.CONFIRM_DELETE_CHOICE

    @property
    def reply_keyboard(self) -> Union[ReplyKeyboardRemove, ReplyKeyboardMarkup]:
        return ReplyKeyboardRemove()

    @property
    def next_state(self) -> int:
        return ConversationHandler.END


class CancellationPresenter(TelegramPresenter):
    def __init__(self, update: Update):
        super().__init__(update)

    @property
    def text(self) -> str:
        return constants.SAY_GOODBYE

    @property
    def reply_keyboard(self) -> Union[ReplyKeyboardRemove, ReplyKeyboardMarkup]:
        return ReplyKeyboardRemove()

    @property
    def next_state(self) -> int:
        return ConversationHandler.END
