import os
import pickle


# todo read priority problem
# todo data schema and it's validation when saving/reading, current data schema is Dict[id, {BOTUSERDTO}]
class DataOperator:
    """
    Performs main app_data operations: load, safe. Concurrently safe.
    tests https://github.com/elarivie/pyReaderWriterLock/blob/master/tests/rwlock_test.py
    """
    def __init__(self, file_name: str):
        self._file: str = os.path.join(os.path.dirname(__file__), file_name)

    def save_data(self, data):
        with open(self._file, 'wb') as cur_f:
            pickle.dump(data, cur_f)

    def data_load(self):
        with open(self._file, 'rb') as cur_f:
            pickled_data: dict = pickle.load(cur_f)
        return pickled_data


class AppDataManager(DataOperator):
    """
    Base data manager
    """
    def __init__(self):
        super().__init__('app_db')


class TestDataManager(DataOperator):
    """
    Data manger for tests
    """
    def __init__(self):
        super().__init__('test_db')


if __name__ == '__main__':
    # todo temporary
    with open(os.path.join(os.path.dirname(__file__), 'app_db'), 'wb') as f:
        pickle.dump(
            {
                304177474: {
                    'user_id': 304177474,
                    'habits': [
                        {
                            'habit_name': 'Перестать есть мучное',
                            'motivational_messages': {
                                1: 'Здравствуй!',
                                2: 'Эти сообщения отправляются автоматически',
                                3: 'Правда происходит это не через три дня, а 5 '
                                   'секунд',
                                4: 'Самое классное - мы можем поменять параметр '
                                   'времени',
                                5: 'А это самое последнее сообщение, оно пятое, но '
                                   'и это мы можем очень просто поменять до 10))'
                            },
                            'state': 1
                        }
                    ]
                },
                # 462920945: {
                #     'user_id': 462920945,
                #     'habits': [
                #         {
                #             'habit_name': 'Перестать есть мучное',
                #             'motivational_messages': {
                #                 1: 'Здравствуй!',
                #                 2: 'Эти сообщения отправляются автоматически',
                #                 3: 'Правда происходит это не через три дня, а 5 '
                #                    'секунд',
                #                 4: 'Самое классное - мы можем поменять параметр '
                #                    'времени',
                #                 5: 'А это самое последнее сообщение, оно пятое, но '
                #                    'и это мы можем очень просто поменять до 10))'
                #             },
                #             'state': 1
                #         }
                #     ]
                # }
            },
            f
        )
