import sys


from test.celery_test_runner import CeleryWorker, CeleryBeat


a = CeleryWorker()
b = CeleryBeat()

print('sys path is', sys.path)
print(a._celery_test_app_name)

a.run()
b.run()
print('Now sleep')
import time
time.sleep(30)
print('wake up')
b.down()
a.down()
