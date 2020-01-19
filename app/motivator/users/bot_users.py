from abc import ABCMeta, abstractmethod

from app.motivator.users.user_dto import UserDTO


class BaseBotUser(metaclass=ABCMeta):
    @abstractmethod
    def greet(self) -> str:
        raise NotImplementedError


class NewBotUser(BaseBotUser):
    def __init__(self, user_id):
        self.user_data = UserDTO(user_id)
        self._greeting = 'wasup mate' # tmp

    def greet(self) -> str:
        return self._greeting


class KnownBotUser(BaseBotUser):
    def __init__(self, user_id, habits):
        self.user_data = UserDTO(user_id, habits)
        self._greeting = 'wasup known mate' # tmp

    def greet(self) -> str:
        return self._greeting
