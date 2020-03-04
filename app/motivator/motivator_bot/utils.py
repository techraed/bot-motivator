from typing import List


def convert_answer_reply_to_regex(user_reply: List[str]) -> str:
    separator: str = '|'
    variants_to_handle: str = separator.join(user_reply)
    return f"^({variants_to_handle})$"
