from typing import List

from app.motivator.constants import MAX_HABITS
from app.motivator.habits.habit import Habit


class UserDTO:
    """
    Найди способ защититься следующим образом:
    чтобы название параметров совпадало с названием атрибутов
    """
    max_habit: int = MAX_HABITS

    def __init__(self, user_id: int, habits: List[Habit] = None):
        self.user_id: int = user_id
        self.habits: List[Habit] = [] if habits is None else habits
        """
        self._results: Dict[Habbit, int] -> рекорд, сколько продержался
        self._sex: str
        self._age
        """

    @property
    def habits_amount(self) -> int:
        return len(self.habits)
