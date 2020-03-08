from abc import ABCMeta, abstractmethod
from typing import Dict, List, Tuple
from datetime import datetime, timedelta

from app.motivator.constants import APP_HABITS
from app.motivator.users.user_dto import UserDTO
from app.motivator.users.habits.habits_data_provider import habits_config_data_provider, HabitsConfigDataProvider


class BaseBotUser(metaclass=ABCMeta):
    def __init__(self, user_id, habits):
        self.now_time: datetime = datetime.now()
        self.user_data: UserDTO = UserDTO(user_id, habits)
        self._habits_data_provider: HabitsConfigDataProvider = habits_config_data_provider

    def add_habit(self, habit: str):
        new_habit_data: Dict = {
            "message_state": 1,
            "time_state": {
                "year": self.now_time.year,
                "month": self.now_time.month,
                "day": self.now_time.day,
                "hour": self.now_time.hour,
                "minute": self.now_time.minute,
                "second": self.now_time.second
            }
        }
        new_habit_data.update(self._habits_data_provider.get_habit_by_name(habit))
        self.user_data.habits.append(new_habit_data)

    def delete_habit(self, habit: str):
        for i in range(len(self.user_data.habits)):
            if self.user_data.habits[i]['habit_name'] == habit:
                self.user_data.habits.pop(i)

    def get_habits(self):
        return self.user_data.user_current_habit_names

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

    def delete_habit(self, habit: str):
        for i in range(len(self.user_data.habits)):
            if self.user_data.habits[i]['habit_name'] == habit:
                self.user_data.habits.pop(i)

    def get_habits(self):
        return self.user_data.user_current_habit_names

    def update_habits_states(self):
        for habit in self.user_data.habits:
            max_habit_state: int = self._habits_data_provider.count_habit_messages(habit['habit_name'])
            habit['message_state'] = None if habit['message_state'] == max_habit_state else habit['message_state'] + 1
            habit['time_state'] = {
                "year": self.now_time.year,
                "month": self.now_time.month,
                "day": self.now_time.day,
                "hour": self.now_time.hour,
                "minute": self.now_time.minute,
                "second": self.now_time.second
            }

    def get_responses(self) -> List[Dict]:
        messages: List[Dict] = []
        habits_for_motivation = self.habits_to_motivate
        for habit in habits_for_motivation:
            actual_message = habit['motivational_messages'][habit['message_state']]
            actual_sticker = habit['motivational_stickers'][habit['message_state']]
            messages.append({'message': actual_message, 'sticker': actual_sticker})
        return messages

    @property
    def habits_to_motivate(self) -> list:
        returning_habits: List = []
        for habit in self.user_data.habits:
            habit_time_state: datetime = datetime(**habit['time_state'])
            after_interval = timedelta(days=3)
            if self.now_time - after_interval >= habit_time_state and self.now_time.hour >= 14:
                returning_habits.append(habit)
        return returning_habits
