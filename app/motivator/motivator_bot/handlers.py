from telegram.ext import Filters, CommandHandler, MessageHandler, Handler

from app.motivator.motivator_bot.handlers_logic.callbacks import start, react_start_choice, react_habit_choice, cancel
from app.motivator.constants import (
    REACT_START_CHOICE, REACT_HABIT_CHOICE, READY_TO_START_ANSWERS, HABITS_CHOICE_ANSWERS
)
from app.motivator.motivator_bot.utils import convert_answer_reply_to_regex


entry_point_start: Handler = CommandHandler('start', start)
start_processor: Handler = MessageHandler(
    Filters.regex(convert_answer_reply_to_regex(READY_TO_START_ANSWERS)),
    react_start_choice
)
habit_choice_processor: Handler = MessageHandler(
    Filters.regex(convert_answer_reply_to_regex(HABITS_CHOICE_ANSWERS)),
    react_habit_choice
)
fallback_cancel: Handler = CommandHandler('cancel', cancel)


conversation_handler_kwargs = {
    'entry_points': [
        entry_point_start
    ],
    'states': {
        REACT_START_CHOICE: [start_processor],
        REACT_HABIT_CHOICE: [habit_choice_processor]
    },
    'fallbacks': [fallback_cancel]
}
