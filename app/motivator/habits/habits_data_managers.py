import os
import yaml
from typing import List, Dict


# todo схема привычки и ее валидация
class HabitConfigsDataCollector:

    def __init__(self):
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        self._config_dir: str = os.path.join(current_dir, 'habits_configs')

    def collect_data(self) -> List[Dict]:
        all_habits_data: list = []
        for habit_file in os.listdir(self._config_dir):
            all_habits_data.append(self._get_habit_config_data(habit_file))

        return all_habits_data

    def _get_habit_config_data(self, habit_file: str) -> Dict:
        with open(os.path.join(self._config_dir, habit_file)) as habit_data:
            return yaml.safe_load(habit_data)


class HabitsDataProvider:
    HABITS_DATA: list = HabitConfigsDataCollector().collect_data()

    @classmethod
    def get_habits_names(cls) -> List[str]:
        return [habit['habit_name'] for habit in cls.HABITS_DATA]

    @classmethod
    def get_habits_amount(cls) -> int:
        return len(cls.HABITS_DATA)
