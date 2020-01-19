from typing import Dict

from app.motivator.habits.base import Habit


class UserDTO:
    """
    Найди способ защититься следующим образом:
    чтобы название параметров совпадало с названием атрибутов
    """
    def __init__(self, user_id: int, habits: Dict[Habit, int] = None):
        self.user_id = user_id
        self.habits: Dict[Habit, int] = habits
        """
        self._habbits: Dict[Habbit, int] -> срок для каждой привычки
        self._results: Dict[Habbit, int] -> рекорд, сколько продержался
        self._sex: str
        self._age
        """
