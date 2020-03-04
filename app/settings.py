import os


class AppSettings:
    ROOT = os.path.dirname(os.path.dirname(__file__))
    TOKEN = os.environ.get('BOT_TOKEN', None)
    assert TOKEN is not None, "Token for the bot isn't provided"
