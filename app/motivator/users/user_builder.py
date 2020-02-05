from typing import Union

from app.motivator.users.utils import UserBuildData
from app.motivator.users.bot_users import NewBotUser, KnownBotUser


class UserBuilder:
    def __init__(self, user_id: int, user_data: dict):
        self._user_id: int = user_id
        self._user_data: dict = user_data

    def build_user(self) -> Union[NewBotUser, KnownBotUser]:
        user_build_data: UserBuildData = self._get_build_data()
        user_class: [Union[NewBotUser, KnownBotUser]] = user_build_data.user_type
        return user_class(**user_build_data.user_data)

    def _get_build_data(self) -> UserBuildData:
        if self._user_data_is_empty():
            return UserBuildData(user_type=NewBotUser, user_data={'user_id': self._user_id, 'habits': None})
        return UserBuildData(user_type=KnownBotUser, user_data=self._user_data)

    def _user_data_is_empty(self) -> bool:
        return not self._user_data
