import os
from typing import List, Tuple, Dict

from celery import Celery

from app.app_data.user_data_manager import user_data_manager
from app.motivator.motivator_bot.telegram_bot import motivator
from app.motivator.users.user_builder import UserBuilder, KnownBotUser


app = Celery('celery_motivator', broker='pyamqp://guest@localhost//', )
path_to_motivate_task = os.path.splitext(__file__)[0]


@app.task(ignore_result=True)
def motivate():
    all_users_data = user_data_manager.get_all_users_data()
    users_data_to_save: List[Tuple[int, Dict]] = []

    for user_id, user_data in all_users_data.items():
        bot_user: KnownBotUser = UserBuilder(user_id, user_data).build_user()
        responses_for_user: list = bot_user.get_responses()

        if responses_for_user:
            for response in responses_for_user:
                motivator.bot.send_message(chat_id=user_id, text=response['message'])
                motivator.bot.send_sticker(chat_id=user_id, sticker=response['sticker'])
            bot_user.update_habits_states()

        users_data_to_save.extend(bot_user.user_data_for_save)
    user_data_manager.update_users_data(users_data_to_save)


app.conf.beat_schedule = {
    "motivate": {
        "task": "app.task_processor.celery_motivator.motivate",
        "schedule": 5.0,
    }
}
