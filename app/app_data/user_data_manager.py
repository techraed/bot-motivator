from typing import Dict, List, Tuple

from readerwriterlock import rwlock

from app.app_data.app_data_manager import AppDataManager


class UserDataManager:
    """
    AppDataManager does not know anything about managing data. It just saves
    it.

    Concerning UserDataManager, it knows that there is user data in storage. It does not know
    any details about it, but it knows some main identifying information, like data fields (attributes),
    data scheme (dict).
    """
    def __init__(self):
        self._db_manager = AppDataManager()
        self._synch_primitive = rwlock.RWLockRead()

    def get_user_data(self, user_id: int) -> dict:
        all_users_data: dict = self.get_all_users_data()
        return all_users_data.get(user_id, {})

    def get_all_users_data(self) -> dict:
        with self._synch_primitive.gen_rlock():
            all_users_data: dict = self._db_manager.data_load()
        return all_users_data

    def update_users_data(self, users_data_for_save: List[Tuple[int, Dict]]):
        with self._synch_primitive.gen_wlock():
            updated_data = self._get_updated_data(users_data_for_save)
            self._db_manager.save_data(updated_data)

    def _get_updated_data(self, update: List[Tuple[int, Dict]]) -> dict:
        current_data: dict = self._db_manager.data_load()
        current_data.update(update)
        return current_data


user_data_manager = UserDataManager()
