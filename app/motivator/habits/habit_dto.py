from typing import Dict


class HabitDTO:
    def __init__(self, habit_name: str, motivational_messages: Dict[int, str]):
        self.habit_name: str = habit_name
        self.motivational_messages: Dict[int, str] = motivational_messages
