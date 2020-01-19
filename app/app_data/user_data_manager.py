from app.app_data.app_data_manager import AppDataManager


class UserDataManager:
    def __init__(self):
        self._db_manager = AppDataManager()

    def get_user_data(self, user_id: int) -> dict:
        user_data: dict = self._db_manager.safe_data_load()
        return user_data.get(user_id, {})

    def save_user_data(self, user_data: dict):
        self._db_manager.safe_data_save(user_data)
