import sys
import signal
from abc import ABCMeta, abstractmethod
from typing import List

import sh

from tests.celery_test import celery_test_app_name # too explicit. why? look at the comment below


class CeleryServiceForTest(metaclass=ABCMeta):
    def __init__(self):
        self._service_command = sh.Command('celery')
        self._running_celery_process = None
        self._celery_test_app_name = f'tests.{celery_test_app_name}' # actually, it should be initialised from func param

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

    def _get_service_args(self) -> List[str]:
        return ['-A', self._celery_test_app_name, 'beat', '-l', 'INFO']


class CeleryWorker(CeleryServiceForTest):
    def __init__(self):
        super().__init__()

    def _get_service_args(self) -> List[str]:
        return ['-A', self._celery_test_app_name, 'worker', '-l', 'INFO']


class CeleryFacadeTester:
    """
    Celery task dumps data to disk (writes integer to file).
    Workers should write to file until integer in the file reaches `max_test_value`
    """
    def __init__(self):
        self.worker = CeleryWorker()
        self.beat = CeleryBeat()

    def __enter__(self):
        self._prepare_test_file()
        self._run_services()
        return self

    @staticmethod
    def _prepare_test_file():
        with open('newfile.txt', 'w') as f:
            f.write('0')

    def _run_services(self):
        self.worker.run()
        self.beat.run()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.beat.down()
        self.worker.down()

