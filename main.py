from app.motivator.motivator_bot.telegram_bot import motivator

# todo script that creates app/db/motivator_data


if __name__ == "__main__":
    motivator.setup()
    motivator.run()
