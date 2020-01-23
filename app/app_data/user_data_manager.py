from typing import Union

from app.app_data.app_data_manager import AppDataManager
from app.motivator.users.bot_users import NewBotUser, KnownBotUser


class UserDataManager:
    def __init__(self):
        self._db_manager = AppDataManager()

    def get_user_data(self, user_id: int) -> dict:
        user_data: dict = self._db_manager.safe_data_load()
        return user_data.get(user_id, {})

    def save_user_data(self, user: Union[NewBotUser, KnownBotUser]):
        self._db_manager.safe_data_update(user.data_for_save)
