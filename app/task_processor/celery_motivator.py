from typing import List, Tuple, Dict

from celery import Celery

from app.app_data.user_data_manager import user_data_manager
from app.motivator.motivator_bot.telegram_bot import motivator
from app.motivator.users.user_builder import UserBuilder, KnownBotUser


app = Celery('celery_motivator', broker='pyamqp://guest@localhost//')


def motivate():
    all_users_data = user_data_manager.get_all_users_data()
    users_to_save: List[Tuple[int, Dict]] = []
    for user_id, user_data in all_users_data.items():
        bot_user: KnownBotUser = UserBuilder(user_id, user_data).build_user()
        for message in bot_user.get_messages():
            motivator.bot.send_message(chat_id=user_id, text=message)
        users_to_save.extend(bot_user.user_data_for_save)
    user_data_manager.update_users_data(users_to_save)


if __name__ == "__main__":
    motivate()