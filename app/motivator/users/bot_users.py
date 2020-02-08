from abc import ABCMeta, abstractmethod
from typing import Dict, List, Tuple

from app.motivator.constants import APP_HABITS
from app.motivator.users.user_dto import UserDTO
from app.motivator.users.habits.habit_message_getter import HabitMessageGetter
from app.motivator.users.habits.habits_data_provider import habits_config_data_provider, HabitsConfigDataProvider


class BaseBotUser(metaclass=ABCMeta):
    def __init__(self, user_id, habits):
        self.user_data: UserDTO = UserDTO(user_id, habits)
        self._habits_config_data_provider: HabitsConfigDataProvider = habits_config_data_provider

    def add_habit(self, habit: str):
        new_habit_data: Dict = {"state": 1}
        new_habit_data.update(habits_config_data_provider.get_habit_by_name(habit))
        self.user_data.habits.append(new_habit_data)

    @abstractmethod
    def can_start(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_available_habits(self) -> List[str]:
        raise NotImplementedError

    @property
    def user_data_for_save(self) -> List[Tuple[int, Dict]]:
        return [(self.user_data.user_id, self.user_data.__dict__)]


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
        available_habits: set = set(APP_HABITS).difference(self.user_data.user_current_habit_names)
        return list(available_habits)

    def get_messages(self) -> List[str]:
        messages: List[str] = []
        for habit in self.user_data.habits:
            messages.append(HabitMessageGetter(habit).get_actual_message())
        return messages
