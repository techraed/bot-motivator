import unittest

from tests.test_utils.start_test_utils import create_test_db_file, delete_test_db_file


class StartHandlerTest(unittest.TestCase):
    # todo test are very dirty
    def setUp(self):
        self.user_id = 123
        create_test_db_file()

    def tearDown(self):
        delete_test_db_file()


if __name__ == '__main__':
    unittest.main()
