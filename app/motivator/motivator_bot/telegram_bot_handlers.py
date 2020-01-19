from app.motivator.users.user_controller import UserController


# todo types of handlers args
def start(update, context):
    user_id = update.message.chat.id
    bot_user = UserController.get_user(user_id)
    return bot_user
    """
    from telegram_bot_controller import greet
    greet(bot_user)
    """
