from abc import ABCMeta, abstractmethod


class BotUserDS:
    def __init__(self, user_id: int):
        self._id = user_id
        """
        self._habbits: Dict[Habbit, int] -> срок для каждой привычки
        self._results: Dict[Habbit, int] -> рекорд, сколько продержался
        self._sex: str
        self._age
        """