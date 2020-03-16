from telegram import Update
from telegram.ext import CallbackContext

from app.motivator.motivator_bot.handlers_logic.presenters import (
    StartPresenter, ShowAvailableHabitsPresenter, ChoiceConfirmPresenter, CancellationPresenter, DeletePresenter,
    ShowUserCurrentHabitsPresenter, DeleteConfirmPresenter, InformationPresenter
)
from app.motivator.motivator_bot.handlers_logic.update_data_handlers import (
    BeginConversationUpdateDataHandler, ShowAvailableHabitsUpdateHandler, ChoiceConfirmUpdateHandler,
    ShowUserCurrentHabitsUpdateHandler, ChoiceDeleteUpdateHandler
)


def start(update: Update, context: CallbackContext) -> int:
    """
    Greets user and asks whether he is ready to add habits, if user
    has adding ability.
    """
    BeginConversationUpdateDataHandler(update, context).handle_data()

    start_presenter = StartPresenter(update, context)
    start_presenter.present_response()
    return start_presenter.next_state


def react_start_choice(update: Update, context: CallbackContext) -> int:
    """
    Called after start. Process user choice, which was done in start handler.
    """
    ShowAvailableHabitsUpdateHandler(update, context).handle_data()

    show_habits_presenter = ShowAvailableHabitsPresenter(update, context)
    show_habits_presenter.present_response()
    return show_habits_presenter.next_state


def react_habit_choice(update: Update, context: CallbackContext) -> int:
    """
    Saves user habit choice and finishes conversation
    """
    ChoiceConfirmUpdateHandler(update, context).handle_data()

    confirm_presenter = ChoiceConfirmPresenter(update)
    confirm_presenter.present_response()
    return confirm_presenter.next_state


def delete(update: Update, context: CallbackContext) -> int:
    """
    Asks whether user is ready to delete habits, if user
    has deleting ability.
    """
    BeginConversationUpdateDataHandler(update, context).handle_data()

    delete_presenter = DeletePresenter(update, context)
    delete_presenter.present_response()
    return delete_presenter.next_state


def react_delete_choice(update: Update, context: CallbackContext) -> int:
    """
    Called after delete.
    """
    ShowUserCurrentHabitsUpdateHandler(update, context).handle_data()

    show_user_habits_presenter = ShowUserCurrentHabitsPresenter(update, context)
    show_user_habits_presenter.present_response()
    return show_user_habits_presenter.next_state


def react_confirm_choice(update: Update, context: CallbackContext) -> int:
    """
    Saves user delete-habit choice and finishes conversation
    """
    ChoiceDeleteUpdateHandler(update, context).handle_data()

    delete_confirm_presenter = DeleteConfirmPresenter(update)
    delete_confirm_presenter.present_response()
    return delete_confirm_presenter.next_state


def cancel(update: Update, context: CallbackContext) -> int:
    cancellation_presenter = CancellationPresenter(update)
    cancellation_presenter.present_response()
    return cancellation_presenter.next_state


def information(update: Update, context: CallbackContext) -> int:
    """
    Provides general information about the bot and commands.
    """
    information_presenter = InformationPresenter(update, context)
    information_presenter.present_response()
    return information_presenter.next_state
