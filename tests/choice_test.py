import unittest
from typing import Union

from app.app_data.user_data_manager import TestUserDataManager
from app.motivator.users.user_builder import UserBuilder, NewBotUser, KnownBotUser
from tests.test_utils.start_test_utils import create_test_db_file, delete_test_db_file


class ChoiceHandlerTest(unittest.TestCase):
    def setUp(self):
        self.user_id = 123
        create_test_db_file()

    def test_adding_data(self):
        chosen_habit: str = 'sport'
        user_data: dict = TestUserDataManager().get_user_data(self.user_id)
        bot_user: Union[NewBotUser, KnownBotUser] = UserBuilder(self.user_id, user_data).build_user()
        bot_user.add_habit(chosen_habit)
        TestUserDataManager().update_users_data(bot_user.user_data_for_save)
        user_data_new: dict = TestUserDataManager().get_user_data(self.user_id)
        #self.assertEqual(user_data_new,chosen_habit )
        print(user_data_new)

    def tearDown(self):
        delete_test_db_file()


if __name__ == '__main__':
    unittest.main()