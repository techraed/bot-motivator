from telegram import Update
from telegram.ext import CallbackContext

from app.motivator.users.user_controller import UserController
from app.motivator.motivator_bot.telegram_bot_presenters import greet


def start(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    bot_user = UserController.get_user(user_id)
    greet(update, bot_user)
