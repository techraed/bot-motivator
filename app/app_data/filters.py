from abc import ABCMeta, abstractmethod


class UserRowFilter(metaclass=ABCMeta):

    @abstractmethod
    def filter(self, data):
        raise NotImplemented


class UserHabitsFilter(UserRowFilter):

    @classmethod
    def filter(cls, user_habits: list):
        for habit in user_habits:
            if cls._is_not_valid_habit(habit):
                user_habits.remove(habit)

    @classmethod
    def _is_not_valid_habit(cls, habit) -> bool:
        return not cls._is_valid_habit(habit)

    @staticmethod
    def _is_valid_habit(habit) -> bool:
        if habit['state'] is not None:
            return True


class UserDataFiltersFacade:
    _habit_filter_class = UserHabitsFilter

    @classmethod
    def filter_data(cls, user_data):
        cls._habit_filter_class.filter(user_data['habits'])
