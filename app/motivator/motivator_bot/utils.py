from typing import List
from app.motivator.motivator_bot.constants import NO


def convert_answer_reply_to_regex(user_reply: List[str]) -> str:
    separator: str = '|'
    variants_to_handle: str = separator.join(user_reply)
    return f"^({variants_to_handle})$"


def is_not_affirmative_choice(answer: str):
    return answer == NO
