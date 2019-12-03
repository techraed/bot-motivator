import time

from test.celery_test_runner import CeleryFacadeTester


with CeleryFacadeTester():
    print('SLEEP')
    time.sleep(30)
    print('WAKE UP TO KILL CELERY')
