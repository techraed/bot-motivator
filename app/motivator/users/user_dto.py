from typing import List

from app.motivator.constants import MAX_HABITS


class UserDTO:
    """
    Найди способ защититься следующим образом:
    чтобы название параметров совпадало с названием атрибутов
    """
    max_habit: int = MAX_HABITS

    def __init__(self, user_id: int, habits: List[str] = None):
        self.user_id: int = user_id
        self.habits: List[str] = [] if habits is None else habits
        """
        self._results: Dict[Habbit, int] -> рекорд, сколько продержался
        self._sex: str
        self._age
        """

    @property
    def habits_amount(self) -> int:
        return len(self.habits)
