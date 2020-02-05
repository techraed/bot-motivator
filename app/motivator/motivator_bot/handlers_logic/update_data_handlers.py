from typing import Union
from abc import ABCMeta, abstractmethod

from telegram import Update
from telegram.ext import CallbackContext

from app.app_data.user_data_manager import user_data_manager
from app.motivator.users.user_builder import UserBuilder, NewBotUser, KnownBotUser


class BaseUpdateDataHandler(metaclass=ABCMeta):
    def __init__(self, update: Update, context: CallbackContext):
        self._update = update
        self._context = context

    @abstractmethod
    def handle_data(self):
        raise NotImplementedError


class StartUpdateDataHandler(BaseUpdateDataHandler):
    def __init__(self, update: Update, context: CallbackContext):
        super().__init__(update, context)
        self._context_user_data: dict = self._context.user_data

    def handle_data(self):
        user_id: int = self._update.message.chat.id
        user_data: dict = user_data_manager.get_user_data(user_id)
        bot_user: Union[NewBotUser, KnownBotUser] = UserBuilder(user_id, user_data).build_user()
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
        bot_user.add_habit(chosen_habit)
        user_data_manager.update_users_data(bot_user.user_data_for_save)
