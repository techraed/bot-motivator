from typing import Union, Type
from abc import ABCMeta, abstractmethod

from telegram import Update
from telegram.ext import CallbackContext

from app.motivator.users.user_controller import UserController
from app.motivator.habits.habit_controller import HabitsController
from app.motivator.users.bot_users import NewBotUser, KnownBotUser


class BaseUpdateDataHandler(metaclass=ABCMeta):
    def __init__(self, update: Update, context: CallbackContext):
        self._update = update
        self._context = context

    @abstractmethod
    def handle_data(self):
        raise NotImplementedError


# UpdateController: Type = Type[BaseUpdateDataHandler]


class StartUpdateDataHandler(BaseUpdateDataHandler):
    def __init__(self, update: Update, context: CallbackContext):
        super().__init__(update, context)
        self._context_user_data: dict = self._context.user_data

    def handle_data(self):
        user_id: int = self._update.message.chat.id
        bot_user: Union[NewBotUser, KnownBotUser] = UserController.get_user(user_id)
        self._context.user_data['bot_user_instance']: Union[NewBotUser, KnownBotUser] = bot_user


class ShowHabitsUpdateHandler(BaseUpdateDataHandler):
    def __init__(self, update: Update, context: CallbackContext):
        super().__init__(update, context)
        self._context_user_data: dict = self._context.user_data

    def handle_data(self):
        user_start_response: str = self._update.message.text
        self._context_user_data['user_start_response']: str = user_start_response


class ChoiceConfirmUpdateHandler(BaseUpdateDataHandler):
    def __init__(self, update: Update, context: CallbackContext):
        super().__init__(update, context)

    def handle_data(self):
        chosen_habit: str = self._update.message.text
        bot_user: Union[NewBotUser, KnownBotUser] = self._context.user_data['bot_user_instance']
        bot_user.add_habit(HabitsController.create_new_habit(chosen_habit))
        UserController.save_user(bot_user)
