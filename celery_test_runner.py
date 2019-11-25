import sys
import signal
from abc import ABCMeta, abstractmethod
from typing import Tuple, List

import sh

from celery_test import celery_test_app_name # too explicit


class CeleryServiceForTest(metaclass=ABCMeta):
    def __init__(self):
        self._service_command = sh.Command('celery')
        self._running_celery_process = None
        self._celery_test_app_name = celery_test_app_name # по хорошему в момент инициализации

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


# напиши простой тест
a = CeleryWorker()
a.run()
print('Now sleep')
import time
time.sleep(15)
print('wake up')
a.down()
