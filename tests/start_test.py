import unittest

from app.app_data.user_data_manager import UserDataManager
from app.app_data.app_data_manager import TestDataManager
from app.motivator.users.user_controller import UserController
from app.motivator.users.bot_users import NewBotUser, KnownBotUser
from tests.test_utils.start_test_utils import create_test_db_file, delete_test_db_file


class TestUserDataManager(UserDataManager):
    def __init__(self):
        self._db_manager = TestDataManager()


class TestUserController(UserController):
    _user_data_manager = TestUserDataManager()


class StartHandlerTest(unittest.TestCase):
    # todo test are very dirty
    def setUp(self):
        self.user_id = 123
        create_test_db_file()

    def test_user_types(self):
        new_user = TestUserController.get_user(self.user_id)
        self.assertEqual(isinstance(new_user, NewBotUser), True)

        TestUserController.save_user(new_user)
        known_user = TestUserController.get_user(self.user_id)
        self.assertEqual(isinstance(known_user, KnownBotUser), True)

    def tearDown(self):
        delete_test_db_file()


if __name__ == '__main__':
    unittest.main()
