from abc import ABCMeta, abstractmethod
from typing import Dict

from app.motivator.users.user_dto import UserDTO


class BaseBotUser(metaclass=ABCMeta):
    def __init__(self, user_id, habits):
        self.user_data: UserDTO = UserDTO(user_id, habits)

    @abstractmethod
    def can_start(self) -> bool:
        raise NotImplementedError

    def can_not_start(self) -> bool:
        # todo do we really need it?
        return not self.can_start()

    @property
    def data_for_save(self) -> Dict[int, dict]:
        return {self.user_data.user_id: self.user_data.__dict__}


class NewBotUser(BaseBotUser):
    def __init__(self, user_id, habits):
        super().__init__(user_id, habits)

    def can_start(self) -> bool:
        return True


class KnownBotUser(BaseBotUser):
    def __init__(self, user_id, habits):
        super().__init__(user_id, habits)

    def can_start(self) -> bool:
        return self.user_data.habits_amount < self.user_data.max_habit
