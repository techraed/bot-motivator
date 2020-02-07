import os
import yaml
from typing import List, Dict


# todo схема привычки и ее валидация
class HabitsConfigsDataCollector:

    def __init__(self):
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        self._config_dir: str = os.path.join(current_dir, 'habits_configs')

    def collect_data(self) -> List[Dict]:
        all_habits_data: List[Dict] = []
        for habit_file in os.listdir(self._config_dir):
            all_habits_data.append(self._get_habit_config_data(habit_file))

        return all_habits_data

    def _get_habit_config_data(self, habit_file: str) -> Dict:
        with open(os.path.join(self._config_dir, habit_file)) as habit_data:
            return yaml.safe_load(habit_data)


class HabitsConfigDataProvider:
    def __init__(self):
        self._habits_data: List[Dict] = HabitsConfigsDataCollector().collect_data()

    def get_habits_names(self) -> List[str]:
        return [habit['habit_name'] for habit in self._habits_data]

    def get_habit_by_name(self, name: str) -> Dict:
        for habit in self._habits_data:
            if habit['habit_name'] == name:
                return habit

    def get_habits_amount(self) -> int:
        return len(self._habits_data)


habits_config_data_provider: HabitsConfigDataProvider = HabitsConfigDataProvider()


if __name__ == '__main__':
    # todo tmp
    import pprint
    pprint.pprint(habits_config_data_provider.get_habit_by_name('Перестать есть мучное'))
