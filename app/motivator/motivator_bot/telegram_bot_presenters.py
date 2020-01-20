from typing import Union

from telegram import Update, ReplyKeyboardMarkup

from app.motivator.users.bot_users import NewBotUser, KnownBotUser
from app.motivator.habits.habits_constants import APP_HABITS


def greet(update: Update, user: Union[NewBotUser, KnownBotUser]):
    reply_keyboard = ReplyKeyboardMarkup([['Да', 'Нет']], one_time_keyboard=True)
    update.message.reply_text(
        text=user.get_greet_message(),
        reply_markup=reply_keyboard
    )
