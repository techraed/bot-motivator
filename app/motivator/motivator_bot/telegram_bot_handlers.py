import logging
from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from app.motivator.users.user_controller import UserController
from app.motivator.motivator_bot.telegram_bot_presenters import greet, say_goodbye
from app.motivator.motivator_bot.telegram_conversation_constants import CHOICE


# todo user_id copy-pasted stuff
def start(update: Update, context: CallbackContext):
    """
    Greets user and asks whether he is ready to add habits, if user
    has adding ability.
    """
    user_id = update.message.chat.id
    bot_user = UserController.get_user(user_id)
    greet(update, bot_user)

    return CHOICE


def choice(update: Update, context: CallbackContext):
    user_id = update.message.chat.id


def cancel(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    logging.info(f"User with chat id {user_id} canceled the conversation.")
    say_goodbye(update)

    return ConversationHandler.END
