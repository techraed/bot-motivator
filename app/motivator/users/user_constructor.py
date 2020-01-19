from typing import Union

from app.motivator.users.bot_users import NewBotUser, KnownBotUser


class UserConstructor:
    def __init__(self):
        self._user_class_types: {str, Union[NewBotUser, KnownBotUser]} = {
            'new': NewBotUser,
            'known': KnownBotUser
        }

    def construct_user(self, user_type, user_data) -> Union[NewBotUser, KnownBotUser]:
        user_class: [Union[NewBotUser, KnownBotUser]] = self._user_class_types[user_type]
        return user_class(**user_data)
