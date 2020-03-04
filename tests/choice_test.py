import unittest
from typing import Union
from datetime import datetime

from app.app_data.user_data_manager import TestUserDataManager
from app.motivator.users.user_builder import UserBuilder, NewBotUser, KnownBotUser
from tests.test_utils.start_test_utils import create_test_db_file, delete_test_db_file


# TODO tests are too tied
class ChoiceHandlerTest(unittest.TestCase):
    def setUp(self):
        self.user_id = 123
        self.key = 'habits'
        self.now_time: datetime = datetime.now()
        self.valid_data = [
            {
                'habit_name': 'Перестать есть мучное',
                'message_state': 1,
                'motivational_messages':
                    {
                        1: "'Жиртрест!' - так тебя будут называть через "
                           'несколько лет! Перестань есть мучное уже.',
                        2: 'Прошлое сообщения тебя взбудоражило, кажется. '
                           'Оно и хорошо, ведь ты уже несколько дней '
                           'держишься без мучного.',
                        3: 'Слушай, а ты молодец! Тебе точно надо ачивки '
                           "давать! Твоя первая ачивка - 'Сильная воля'.",
                        4: 'Ну вот и кончилось мое воображение.'
                    },
                'motivational_stickers':
                    {
                        1: 'CAACAgIAAxkBAAIDcl5ATIFj3G5mlHYAAUnqrQy1WexR0gACewIAAgk7OxNZgdzEcocsihgE',
                        2: 'CAACAgIAAxkBAAIDhF5AT7Hx_a7LBliztr-1sqXavM90AAJSAgACCTs7E46JbCIHDIpfGAQ',
                        3: 'CAACAgIAAxkBAAIDg15AT3PZ9B9_7PrwsFYvZO3458-0AAJuAgACCTs7E2tp7UhrBKbWGAQ',
                        4: 'CAACAgIAAxkBAAIDhV5AT-pbLJJxPr7qGBWaAUS5bChgAAKCAgACCTs7Extmv-eYI2c_GAQ'
                    },
                "time_state":
                    {
                        "year": self.now_time.year,
                        "month": self.now_time.month,
                        "day": self.now_time.day,
                        "hour": self.now_time.hour,
                        "minute": self.now_time.minute,
                        "second": self.now_time.second
                    }
            }
        ]
        create_test_db_file()

    def test_adding_data(self):
        user_data: dict = TestUserDataManager().get_user_data(self.user_id)
        bot_user: Union[NewBotUser, KnownBotUser] = UserBuilder(self.user_id, user_data).build_user()
        chosen_habit: str = "Перестать есть мучное"
        bot_user.add_habit(chosen_habit)
        TestUserDataManager().update_users_data(bot_user.user_data_for_save)
        user_data_new: dict = TestUserDataManager().get_user_data(self.user_id)
        self.assertEqual(self.valid_data, user_data_new['habits'])

    def tearDown(self):
        delete_test_db_file()


if __name__ == '__main__':
    unittest.main()
