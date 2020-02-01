from app.motivator.motivator_bot.telegram_bot import motivator

# todo script that creates app/app_data/app_db (or check it in __new__)
# todo better typing!


if __name__ == "__main__":
    motivator.setup()
    motivator.run()
