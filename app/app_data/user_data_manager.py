from typing import Dict

from app.app_data.app_data_manager import AppDataManager


class UserDataManager:
    """
    AppDataManager does not know anything about managing data. It just saves
    it all in dict. So, the only things it knows: how to work with file, what (dict)
    to save in file.

    Concerning UserDataManager, it knows that there is user data in storage. It does not know
    any details about it, but it knows some main identifying information, like primary keys (pk).
    For example, users pk is his telegram id (aka `user_id`), so UserDataManager knows about that.
    """
    def __init__(self):
        self._db_manager = AppDataManager()

    def get_user_data(self, user_id: int) -> dict:
        user_data: dict = self._db_manager.safe_data_load()
        return user_data.get(user_id, {})

    def save_user_data(self, user_data_for_save: Dict[int, dict]):
        # todo валидация сохраняемых данных
        self._db_manager.safe_data_update(user_data_for_save)
