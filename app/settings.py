import os


class AppSettings:
    ROOT = os.path.dirname(os.path.dirname(__file__))
    TOKEN = os.environ.get('BOT_TOKEN')

