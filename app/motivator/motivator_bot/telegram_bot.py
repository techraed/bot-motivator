import logging

from telegram import Bot
from telegram.ext import Updater, CommandHandler

from app.motivator.motivator_bot.telegram_bot_handlers import start
from app.settings import AppSettings


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


class MotivatorBot:
    # todo assertions, better config handling
    # why use_context?
    def __init__(self):
        self.token = AppSettings.TOKEN
        self.updater = Updater(token=self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

    def setup(self):
        start_handler = CommandHandler('start', start)

        self.dispatcher.add_handler(start_handler)

    def run(self):
        self.updater.start_polling()
        self.updater.idle()

    @property
    def bot(self):
        return Bot(token=self.token)


motivator = MotivatorBot()
