from typing import Union

from telegram import Update, ReplyKeyboardMarkup

from app.motivator.users.bot_users import NewBotUser, KnownBotUser
from app.motivator.motivator_bot import telegram_conversation_constants


def greet(update: Update, user: Union[NewBotUser, KnownBotUser]):
    """
    update.message.reply_text shortcut for bot.send_message -> does not return! That's why if_else
    """
    if user.can_start():
        reply_keyboard = ReplyKeyboardMarkup([['Да', 'Нет']], one_time_keyboard=True)
        update.message.reply_text(
            text=_get_typed_user_greet_message(user),
            reply_markup=reply_keyboard
        )
    else:
        update.message.reply_text(text=telegram_conversation_constants.CANT_START_GREETING)


def _get_typed_user_greet_message(user: Union[NewBotUser, KnownBotUser]) -> str:
    """todo potentially excessive. what if there are multiple user types? the only solution I saw was storing greet
        message in User class, but it's wrong
    """
    if isinstance(user, NewBotUser):
        return telegram_conversation_constants.NEW_USER_GREETING
    return telegram_conversation_constants.KNOWN_USER_GREETING
