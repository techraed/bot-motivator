import unittest
from typing import Union

from app.app_data.user_data_manager import TestUserDataManager
from app.motivator.users.user_builder import UserBuilder, NewBotUser, KnownBotUser
from tests.test_utils.start_test_utils import create_test_db_file, delete_test_db_file


class StartHandlerTest(unittest.TestCase):
    def setUp(self):
        self.user_id = 123
        create_test_db_file()

    def test_user_types(self):
        user_data: dict = TestUserDataManager().get_user_data(self.user_id)
        bot_user: Union[NewBotUser, KnownBotUser] = UserBuilder(self.user_id, user_data).build_user()
        self.assertEqual(isinstance(bot_user, NewBotUser), True)
        self.assertEqual(isinstance(bot_user, KnownBotUser), False)

        TestUserDataManager().update_users_data(bot_user.user_data_for_save)
        user_data: dict = TestUserDataManager().get_user_data(self.user_id)
        bot_user: Union[NewBotUser, KnownBotUser] = UserBuilder(self.user_id, user_data).build_user()
        self.assertEqual(isinstance(bot_user, NewBotUser), False)
        self.assertEqual(isinstance(bot_user, KnownBotUser), True)

    def tearDown(self):
        delete_test_db_file()


if __name__ == '__main__':
    unittest.main()
