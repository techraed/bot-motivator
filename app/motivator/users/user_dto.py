from typing import List, Dict

from app.motivator.constants import MAX_HABITS


class UserDTO:
    max_habit: int = MAX_HABITS

    def __init__(self, user_id: int, habits: List[Dict[str, int]] = None):
        self.user_id: int = user_id
        self.habits: List[Dict[str, int]] = [] if habits is None else habits
        """
        self._results: Dict[Habbit, int] -> рекорд, сколько продержался
        self._sex: str
        self._age
        """

    @property
    def habits_amount(self) -> int:
        return len(self.habits)

    @property
    def user_current_habit_names(self):
        return [habit_name for habit in self.habits for habit_name in habit.keys()]
