from typing import List

from app.motivator.habits.stop_eating_flour import StopEatingFlour


ALL_HABITS = [StopEatingFlour]
ALL_HABITS_NAMES: List[str] = [habit.HABIT_NAME for habit in ALL_HABITS]
