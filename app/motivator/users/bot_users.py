from abc import ABCMeta, abstractmethod
from typing import Dict, List, Set

from app.motivator.users.user_dto import UserDTO, Habit
from app.motivator.constants import APP_HABITS


class BaseBotUser(metaclass=ABCMeta):
    def __init__(self, user_id, habits):
        self.user_data: UserDTO = UserDTO(user_id, habits)

    def add_habit(self, habit: Habit):
        self.user_data.habits.append(habit)

    @abstractmethod
    def can_start(self) -> bool:
        raise NotImplementedError

    def can_not_start(self) -> bool:
        # todo do we really need it?
        return not self.can_start()

    @abstractmethod
    def get_available_habits(self) -> List[str]:
        raise NotImplementedError

    @property
    def user_data_for_save(self) -> Dict[int, dict]:
        return {self.user_data.user_id: self.user_data.__dict__}


class NewBotUser(BaseBotUser):
    def __init__(self, user_id, habits):
        super().__init__(user_id, habits)

    def can_start(self) -> bool:
        return True

    def get_available_habits(self) -> List[str]:
        return APP_HABITS


class KnownBotUser(BaseBotUser):
    def __init__(self, user_id, habits):
        super().__init__(user_id, habits)

    def can_start(self) -> bool:
        return self.user_data.habits_amount < self.user_data.max_habit

    def get_available_habits(self) -> List[str]:
        current_user_habits: Set[str] = {habit.format_name_for_telegram() for habit in self.user_data.habits}
        available_habits: set = set(APP_HABITS).difference(current_user_habits)
        return list(available_habits)
