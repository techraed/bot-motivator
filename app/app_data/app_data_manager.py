import os
import pickle
from readerwriterlock import rwlock


# todo read priority problem
# todo data schema and it's validation when saving/reading, current data schema is Dict[id, {BOTUSERDTO}]
class ApplicationDataOperator:
    """
    Performs main app_data operations: load, safe. Concurrently safe.
    tests https://github.com/elarivie/pyReaderWriterLock/blob/master/tests/rwlock_test.py
    """
    def __init__(self, file_name: str):
        self._file: str = os.path.join(os.path.dirname(__file__), file_name)
        self._synch_primitive = rwlock.RWLockRead()

    def safe_data_update(self, data: dict):
        with self._synch_primitive.gen_wlock():
            updated_data = self._get_updated_data(data)
            self._save_data(updated_data)

    def _get_updated_data(self, update: dict) -> dict:
        current_data: dict = self._data_load()
        current_data.update(update)
        return current_data

    def _save_data(self, data):
        with open(self._file, 'wb') as f:
            pickle.dump(data, f)

    def safe_data_load(self) -> dict:
        with self._synch_primitive.gen_rlock():
            data: dict = self._data_load()
        return data

    def _data_load(self) -> dict:
        with open(self._file, 'rb') as f:
            pickled_data: dict = pickle.load(f)
        return pickled_data


class AppDataManager(ApplicationDataOperator):
    """
    Base data manager
    """
    def __init__(self):
        super().__init__('app_db')


class TestDataManager(ApplicationDataOperator):
    """
    Data manger for tests
    """
    def __init__(self):
        super().__init__('test_db')


if __name__ == '__main__':
    # todo temporary
    with open(os.path.join(os.path.dirname(__file__), 'app_db'), 'wb') as f:
        pickle.dump({304177474: {'user_id': 304177474, 'habits': ['LOL']}}, f)
