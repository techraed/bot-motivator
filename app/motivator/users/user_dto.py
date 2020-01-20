from typing import List, Dict

from app.motivator.habits.base import Habit


class UserDTO:
    """
    Найди способ защититься следующим образом:
    чтобы название параметров совпадало с названием атрибутов
    """
    def __init__(self, user_id: int, habits: List[Habit] = None):
        self.user_id = user_id
        self.habits: List[Habit] = [] if habits is None else habits
        """
        self._results: Dict[Habbit, int] -> рекорд, сколько продержался
        self._sex: str
        self._age
        """

    def get_data_for_save(self) -> Dict[int, dict]:
        return {self.user_id: self.__dict__}
