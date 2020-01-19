import os
import pickle
from readerwriterlock import rwlock


# todo read priority problem
class ApplicationDataOperator:
    """
    Performs main app_data operations: load, safe. Concurrently safe.
    tests https://github.com/elarivie/pyReaderWriterLock/blob/master/tests/rwlock_test.py
    """
    def __init__(self, file_name: str):
        self._file: str = os.path.join(os.path.dirname(__file__), file_name)
        self._synch_primitive = rwlock.RWLockRead()

    def safe_data_save(self, data):
        with self._synch_primitive.gen_wlock():
            self._save_data(data)

    def _save_data(self, data):
        with open(self._file, 'wb') as f:
            pickle.dump(data, f)

    def safe_data_load(self):
        with self._synch_primitive.gen_rlock():
            data = self._data_load()
        return data

    def _data_load(self):
        with open(self._file, 'rb') as f:
            pickled_data = pickle.load(f)
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
