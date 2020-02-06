from typing import Dict


class HabitMessageGetter:
    def __init__(self, habit_data: Dict):
        self._habit_data: Dict = habit_data

    def get_actual_message(self) -> str:
        habit_actual_state: int = self._habit_data['state']
        messages_dict: Dict = self._habit_data['motivational_messages']

        self._update_habit_state()
        return messages_dict[habit_actual_state]

    # todo decorator
    def _update_habit_state(self):
        max_state = self._get_max_habit_state()
        self._habit_data['state'] = None if self._habit_data['state'] == max_state else self._habit_data['state'] + 1

    def _get_max_habit_state(self):
        messages_dict: Dict = self._habit_data['motivational_messages']
        return max(messages_dict.keys())
