from pathlib import Path

from celery import Celery


celery_test_app_name = Path(__file__).stem
app = Celery(celery_test_app_name, broker='pyamqp://guest@localhost//')

@app.task
def sup():
    return 'Sup!'


app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": f"test.{celery_test_app_name}.sup",
        "schedule": 10.0,
    }
}