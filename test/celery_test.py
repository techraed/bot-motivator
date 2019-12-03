from pathlib import Path

from celery import Celery


celery_test_app_name = Path(__file__).stem
app = Celery(celery_test_app_name, broker='pyamqp://guest@localhost//')

@app.task
def sup():
    """
    very bad code only for tests
    """
    with open('newfile.txt', 'r') as f:
        value = f.read()

    if int(value) != 3:
        print('i will increase the value', value)
        with open('newfile.txt', 'w') as f:
            f.write(str(int(value)+1))
    else:
        return 'LOL!'


app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": f"test.{celery_test_app_name}.sup",
        "schedule": 5.0,
    }
}