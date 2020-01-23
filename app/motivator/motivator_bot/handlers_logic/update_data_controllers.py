from typing import Union, Type
from abc import ABCMeta, abstractmethod

from telegram import Update
from telegram.ext import CallbackContext

from app.motivator.users.user_controller import UserController
from app.motivator.users.bot_users import NewBotUser, KnownBotUser


class BaseUpdateDataHandler(metaclass=ABCMeta):
    def __init__(self, update: Update, context: CallbackContext = None):
        self._update = update
        self._context = context

    @abstractmethod
    def handle_data(self):
        raise NotImplementedError


UpdateController: Type = Type[BaseUpdateDataHandler]


class StartUpdateDataHandler(BaseUpdateDataHandler):
    def __init__(self, update: Update, context: CallbackContext):
        super().__init__(update, context)
        self._context_user_data: dict = self._context.user_data

    def handle_data(self):
        user_id: int = self._update.message.chat.id
        bot_user: Union[NewBotUser, KnownBotUser] = UserController.get_user(user_id)
        self._context.user_data['bot_user_class']: Union[NewBotUser, KnownBotUser] = bot_user
