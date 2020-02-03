from typing import Dict

from app.motivator.habits.base import Habit


# todo как сделать жестче структуру класса? В частности HABIT_NAME должен быть у всех субклассов Хэбита
class StopEatingFlour(Habit):
    HABIT_NAME: str = 'Перестать кушать мучное'

    def __init__(self):
        messages: Dict[int, str] = {
            1: "Твое первое сообщение",
            2: "Твое второе сообщение"
        }
        super().__init__(self.HABIT_NAME, messages)
