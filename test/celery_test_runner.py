import sys
import signal
from abc import ABCMeta, abstractmethod
from typing import List

import sh

from test.celery_test import celery_test_app_name # too explicit


class CeleryServiceForTest(metaclass=ABCMeta):
    def __init__(self):
        self._service_command = sh.Command('celery')
        self._running_celery_process = None
        self._celery_test_app_name = f'test.{celery_test_app_name}' # по хорошему в момент инициализации

    def down(self):
        self._running_celery_process.signal(signal.SIGINT)

    def run(self):
        running_celery_service = self._run_celery_service_cmd()
        self._running_celery_process = running_celery_service.process

    def _run_celery_service_cmd(self) -> sh.RunningCommand:
        service_args = self._get_service_args()
        running_service = self._service_command(*service_args, _out=sys.stdout, _err=sys.stderr, _bg=True)
        return running_service

    @abstractmethod
    def _get_service_args(self) -> List[str]:
        raise NotImplementedError()


class CeleryBeat(CeleryServiceForTest):
    def __init__(self):
        super().__init__()

    # может измениться, сделать более общим
    def _get_service_args(self) -> List[str]:
        return ['-A', self._celery_test_app_name, 'beat', '-l', 'INFO']


class CeleryWorker(CeleryServiceForTest):
    def __init__(self):
        super().__init__()

    # может измениться, сделать более общим
    def _get_service_args(self) -> List[str]:
        return ['-A', self._celery_test_app_name, 'worker', '-l', 'INFO']


# import pkgutil
# search_path = ['.'] # set to None to see all modules importable from sys.path
# all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
# print(all_modules)
