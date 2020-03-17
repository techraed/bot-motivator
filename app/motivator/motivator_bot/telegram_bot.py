import logging

from telegram import Bot
from telegram.ext import Updater, ConversationHandler

from app.settings import AppSettings
from app.motivator.motivator_bot.handlers import (
    register_habits_conv_handler_kwargs, delete_habits_conv_handler_kwargs, help_handler
)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class MotivatorBot:
    # todo logging
    def __init__(self):
        self.token = AppSettings.TOKEN
        self.updater = Updater(token=self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

    def setup(self):
        register_habits_conv_handler = ConversationHandler(**register_habits_conv_handler_kwargs)
        delete_habits_conv_handler = ConversationHandler(**delete_habits_conv_handler_kwargs)

        self.dispatcher.add_handler(help_handler)
        self.dispatcher.add_handler(register_habits_conv_handler)
        self.dispatcher.add_handler(delete_habits_conv_handler)

    def run(self):
        self.updater.start_polling()
        self.updater.idle()

    @property
    def bot(self):
        return Bot(token=self.token)


motivator = MotivatorBot()
