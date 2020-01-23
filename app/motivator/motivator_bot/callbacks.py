from typing import Union

from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from app.motivator.users.user_controller import UserController
from app.motivator.users.bot_users import NewBotUser, KnownBotUser
from app.motivator.habits.base import Habit
from app.motivator.motivator_bot.presenters import TelegramPresenter, StartPresenter, show_habits, cancellation_goodbye, confirm_choice
from app.motivator.motivator_bot.constants import REACT_HABIT_CHOICE
from app.motivator.motivator_bot.utils import is_not_affirmative_choice


# todo is it clean to throw in presenters an Update instance?
# todo are context.user_data operations clean? May be Presenter classes can solve the problem (handle_update_data)
def start(update: Update, context: CallbackContext) -> int:
    """
    Greets user and asks whether he is ready to add habits, if user
    has adding ability.
    """

    start_presenter: TelegramPresenter = StartPresenter(update, context)
    start_presenter.run_presenter()
    return start_presenter.get_next_state()


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
    chosen_habit: str = update.message.text
    bot_user: Union[NewBotUser, KnownBotUser] = context.user_data['bot_user']
    bot_user.user_data.habits.append(Habit(chosen_habit))
    UserController.save_user(bot_user)

    confirm_choice(update)

    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    cancellation_goodbye(update)
    return ConversationHandler.END
