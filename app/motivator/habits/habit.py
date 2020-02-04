from typing import Dict

from app.motivator.habits.habit_dto import HabitDTO


class Habit:
    def __init__(self, habit_name: str, motivational_messages: Dict[int, str]):
        self._habit_data = HabitDTO(habit_name, motivational_messages)

    def get_message_for_day(self, day_number: int) -> str:
        return self._habit_data.motivational_messages[day_number]

    def format_name_for_telegram(self) -> str:
        return self._habit_data.habit_name
