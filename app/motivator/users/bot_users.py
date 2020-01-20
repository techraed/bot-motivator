from typing import Dict
from abc import ABCMeta, abstractmethod

from app.motivator.users.user_dto import UserDTO
from app.motivator.users.user_conversation_constants import NEW_USER_GREETING, KNOWN_USER_GREETING


class BaseBotUser(metaclass=ABCMeta):
    def __init__(self, user_id, habits, greeting_message: str):
        self.user_data: UserDTO = UserDTO(user_id, habits)
        self._greeting_message: str = greeting_message

    @abstractmethod
    def get_greet_message(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def has_habits(self) -> bool:
        raise NotImplementedError

    def has_not_habits(self) -> bool:
        return not self.has_habits()


class NewBotUser(BaseBotUser):
    def __init__(self, user_id, habits):
        super().__init__(user_id, habits, NEW_USER_GREETING)

    def get_greet_message(self) -> str:
        return self._greeting_message

    def has_habits(self):
        return False


class KnownBotUser(BaseBotUser):
    def __init__(self, user_id, habits):
        super().__init__(user_id, habits, KNOWN_USER_GREETING)

    def get_greet_message(self) -> str:
        return self._greeting_message

    def has_habits(self) -> bool:
        return len(self.user_data.habits) > 0
