import os
from pathlib import Path

from celery import Celery

from app.motivator.motivator_bot.telegram_bot import motivator


celery_test_app_name = Path(__file__).stem
app = Celery(celery_test_app_name, broker='pyamqp://guest@localhost//')


@app.task
def sup():
    """
    very bad code only for tests
    """
    return motivator.bot.send_message(chat_id=os.environ.get('SAB_ID'), text="HEY")


app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": f"tests.{celery_test_app_name}.sup",
        "schedule": 5.0,
    }
}

# test script
# if __name__ == '__main__':
# import sys
# with CeleryFacadeTester():
#     print('SLEEP')
#     time.sleep(30)
#     print('WAKE UP TO KILL CELERY')
