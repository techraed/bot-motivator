from app.motivator.motivator_bot.telegram_bot_handlers import start


class Chat:
    def __init__(self, id):
        self.id = id


class MessageTestObject:
    def __init__(self, chat_id):
        self.chat = Chat(chat_id)


class UpdateTestObject:
    def __init__(self, chat_id):
        self.message = MessageTestObject(chat_id)


if __name__ == '__main__':
    update = UpdateTestObject(456)
    context = None
    b = start(update, context)
    print(b.greet())
    update = UpdateTestObject(123)
    context = None
    c = start(update, context)
    print(c.greet())
