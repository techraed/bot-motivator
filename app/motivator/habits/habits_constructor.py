from app.motivator.habits.habit import Habit


# todo валидируй схему инпута в construct
class HabitConstructor:

    @classmethod
    def construct(cls, habit_data):
        return Habit(**habit_data)
