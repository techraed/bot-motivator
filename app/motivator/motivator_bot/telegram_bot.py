import logging

from telegram import Bot
from telegram.ext import Updater, ConversationHandler

from app.settings import AppSettings
from app.motivator.motivator_bot.handlers import conversation_handler_kwargs, conversation_handler_delete_kwargs


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class MotivatorBot:
    # todo logging
    def __init__(self):
        self.token = AppSettings.TOKEN
        self.updater = Updater(token=self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

    def setup(self):
        register_conv_handler = ConversationHandler(**conversation_handler_kwargs)
        self.dispatcher.add_handler(register_conv_handler)
        register_conv_delete_handler = ConversationHandler(**conversation_handler_delete_kwargs)
        self.dispatcher.add_handler(register_conv_delete_handler)

    def run(self):
        self.updater.start_polling()
        self.updater.idle()

    @property
    def bot(self):
        return Bot(token=self.token)


motivator = MotivatorBot()
