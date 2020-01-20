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

# todo возможно, лучще сделать классы презентаров. метод greet вызывает can_start. далее, исходя из bool ретерна
# возвращает ответ (также добавляется ветка проверки того, какого типа этот юзер)
# ответы помести в telegram_conversation_constantsи удали соотв user_conv_constants