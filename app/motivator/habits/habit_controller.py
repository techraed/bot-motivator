from typing import Dict

from app.motivator.habits.habits_constructor import HabitConstructor, Habit
from app.motivator.habits.habits_config_data_managers import habits_config_data_provider, HabitsConfigDataProvider


class HabitsController:
    _habit_constructor: HabitConstructor = HabitConstructor
    _habits_data_provider: HabitsConfigDataProvider = habits_config_data_provider

    @classmethod
    def create_new_habit(cls, habit_name: str) -> Habit:
        data_for_new_habit: Dict = cls._habits_data_provider.get_habit_by_name(habit_name)
        new_habit: Habit = cls._habit_constructor.construct(data_for_new_habit)

        return new_habit
