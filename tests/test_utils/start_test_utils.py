import os
from pathlib import Path
from pickle import dump

from app.settings import AppSettings

test_db_path = os.path.join(AppSettings.ROOT, 'app', 'app_data', 'test_db')


def create_test_db_file():
    global test_db_path
    with open(test_db_path, 'wb') as f:
        dump({}, f)


def delete_test_db_file():
    global test_db_path
    Path(test_db_path).unlink()

