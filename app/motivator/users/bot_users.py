from abc import ABCMeta, abstractmethod

from app.motivator.users.user_dto import UserDTO
from app.motivator.habits.habits_constants import MAX_HABITS


class BaseBotUser(metaclass=ABCMeta):
    def __init__(self, user_id, habits):
        self.user_data: UserDTO = UserDTO(user_id, habits)
        self._max_habits = MAX_HABITS

    @abstractmethod
    def can_start(self) -> bool:
        raise NotImplementedError

    def can_not_start(self) -> bool:
        # todo do we really need it?
        return not self.can_start()


class NewBotUser(BaseBotUser):
    def __init__(self, user_id, habits):
        super().__init__(user_id, habits)

    def can_start(self) -> bool:
        return True


class KnownBotUser(BaseBotUser):
    def __init__(self, user_id, habits):
        super().__init__(user_id, habits)

    def can_start(self) -> bool:
        return self.user_data.habits_amount < self._max_habits
