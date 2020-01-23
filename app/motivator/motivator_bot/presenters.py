from typing import Union, List

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove

from app.motivator.users.bot_users import NewBotUser, KnownBotUser
from app.motivator.motivator_bot import constants


# todo clean it! May be with abstract Presenter/
def greet(update: Update, user: Union[NewBotUser, KnownBotUser]):
    """
    update.message.reply_text shortcut for bot.send_message -> does not return! That's why if/else is used
    """
    if user.can_start():
        user_answer_choices: List[List[str]] = [constants.READY_TO_START_ANSWERS]
        reply_keyboard = ReplyKeyboardMarkup(user_answer_choices, one_time_keyboard=True)
        update.message.reply_text(
            text=_get_typed_user_greet_message(user),
            reply_markup=reply_keyboard
        )
    else:
        update.message.reply_text(text=constants.CANT_START_GREETING)


def _get_typed_user_greet_message(user: Union[NewBotUser, KnownBotUser]) -> str:
    """todo potentially excessive. what if there are multiple user types? The only solution I saw was storing greet
        message in User class, but it's does not suit logic
    """
    if isinstance(user, NewBotUser):
        return constants.NEW_USER_GREETING
    return constants.KNOWN_USER_GREETING


def say_goodbye(update: Update):
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
