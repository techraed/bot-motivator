from typing import List, Dict

from app.motivator.constants import MAX_HABITS


class UserDTO:
    max_habit: int = MAX_HABITS

    def __init__(self, user_id: int, habits: List[Dict] = None):
        self.user_id: int = user_id
        self.habits: List[Dict] = [] if habits is None else habits
        """
        self._results: Dict[Habbit, int] -> рекорд, сколько продержался
        self._sex: str
        self._age
        """

    @property
    def habits_amount(self) -> int:
        return len(self.habits)

    # TODO db schema
    @property
    def user_current_habit_names(self) -> List[str]:
        return [habit['habit_name'] for habit in self.habits]
