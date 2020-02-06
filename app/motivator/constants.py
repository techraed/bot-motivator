from typing import List

from app.motivator.users.habits.habits_data_provider import habits_config_data_provider

# habit related constants
APP_HABITS: List[str] = habits_config_data_provider.get_habits_names()
MAX_HABITS = habits_config_data_provider.get_habits_amount()


# bot related constants
REACT_START_CHOICE, REACT_HABIT_CHOICE = range(2)

NEW_USER_GREETING = 'Привет, новичок! Я мотивирую людей бросить что-то или начать. Готов начать?'

KNOWN_USER_GREETING = 'Рад видеть снова! Хочешь добавить привычку?'

CANT_START_GREETING = 'Простите, у Вас полный список привычек в ходу. Вы должны удалить хотя бы одну привычку или ' \
                      'дождаться завершения '

YES = 'Да'

NO = 'Нет'

READY_TO_START_ANSWERS = [YES, NO]

CHOOSE_HABITS = "Отлично! Выбирай привычку."

HABITS_CHOICE_ANSWERS = APP_HABITS

CONFIRM_CHOICE = "Принял. Удачи в этом деле!"

SAY_GOODBYE = "Рад был, что зашел :)"
