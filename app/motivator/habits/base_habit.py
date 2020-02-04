from typing import Dict


class Habit:
    def __init__(self, habit_name: str, motivational_messages: Dict[int, str]):
        self._habit_name: str = habit_name
        self._motivational_messages: Dict[int, str] = motivational_messages

    def get_message_for_day(self, day_number: int) -> str:
        return self._motivational_messages[day_number]

    def format_name_for_telegram(self) -> str:
        return self._habit_name
