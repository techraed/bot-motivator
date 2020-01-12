import pickle
from readerwriterlock import rwlock


# todo типы, read priority problem


class MotivatorDB:
    def __init__(self):
        self._file = 'motivator_data'
        self._synch_primitive = rwlock.RWLockRead()

    def safe_data_save(self, data):
        with self._synch_primitive.gen_wlock():
            self._save_data(data)

    def _save_data(self, data):
        with open(self._file, 'wb') as f:
            pickle.dump(data, f)

    def safe_data_load(self):
        # todo return type?!
        with self._synch_primitive.gen_rlock():
            data = self._data_load()
        return data

    def _data_load(self):
        # todo return type?!
        with open(self._file, 'rb') as f:
            pickled_data = pickle.load(f)
        return pickled_data


motivator_persistence = MotivatorDB()
