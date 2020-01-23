from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from app.motivator.users.user_controller import UserController
from app.motivator.motivator_bot.telegram_bot_presenters import greet, show_habits, say_goodbye
from app.motivator.motivator_bot.constants import REACT_START_CHOICE, REACT_HABIT_CHOICE
from app.motivator.motivator_bot.utils import is_not_affirmative_choice


# todo is it clean to throw in presenters an Update instance?
def start(update: Update, context: CallbackContext) -> int:
    """
    Greets user and asks whether he is ready to add habits, if user
    has adding ability.
    """
    user_id: int = update.message.chat.id
    bot_user = UserController.get_user(user_id)
    greet(update, bot_user)

    return REACT_START_CHOICE


def react_start_choice(update: Update, context: CallbackContext) -> int:
    """
    Called after start. Process user choice, which was done in start handler.
    """
    user_choice: str = update.message.text
    if is_not_affirmative_choice(user_choice):
        return cancel(update, context)
    show_habits(update)

    return REACT_HABIT_CHOICE


def react_habit_choice(update: Update, context: CallbackContext) -> int:
    # todo
    print('was here')
    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    say_goodbye(update)
    return ConversationHandler.END