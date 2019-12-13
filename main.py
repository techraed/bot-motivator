import time

from app.telegram_bot import MotivatorBot


if __name__ == "__main__":
    bot = MotivatorBot()
    bot.setup()
    bot.run()
