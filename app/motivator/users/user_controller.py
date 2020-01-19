from typing import Union

from app.app_data.user_data_manager import UserDataManager
from app.motivator.users.user_constructor import UserConstructor
from app.motivator.users.bot_users import NewBotUser, KnownBotUser


class UserController:
    _user_data_manager = UserDataManager()
    _user_constructor = UserConstructor()

    @classmethod
    def get_user(cls, user_id: int) -> Union[NewBotUser, KnownBotUser]:
        user_data: dict = cls._user_data_manager.get_user_data(user_id)
        if user_data == {}:
            return cls._user_constructor.construct_user(
                user_type='new',
                user_data={'user_id': user_id}
            )
        return cls._user_constructor.construct_user(
            user_type='known',
            user_data=user_data
        )

    @classmethod
    def save_user(cls, user: Union[NewBotUser, KnownBotUser]):
        cls._user_data_manager.save_user_data(user.user_data.__dict__)
