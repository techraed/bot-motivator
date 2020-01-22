import logging

from telegram import Bot
from telegram.ext import Filters, Updater, CommandHandler, ConversationHandler, MessageHandler

from app.settings import AppSettings
from app.motivator.motivator_bot.telegram_bot_handlers import start, choice, cancel
from app.motivator.motivator_bot.telegram_conversation_constants import CHOICE


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


class MotivatorBot:
    # todo assertions, better config handling
    # todo logging
    # todo make an util function to converts constant replies into format, suitable to Filters.regex. Look at presenters
    def __init__(self):
        self.token = AppSettings.TOKEN
        self.updater = Updater(token=self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

    def setup(self):
        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start)],
            states={
                CHOICE: [MessageHandler(Filters.regex('^(Да|Нет)$'), choice)]
            },
            fallbacks=[CommandHandler('cancel', cancel)]
        )

        self.dispatcher.add_handler(conversation_handler)

    def run(self):
        self.updater.start_polling()
        self.updater.idle()

    @property
    def bot(self):
        return Bot(token=self.token)


motivator = MotivatorBot()
