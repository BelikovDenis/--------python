import string


def count_punct_marks(text: str) -> int:
    total_count = 0
    for sym in string.punctuation:
        total_count += text.count(sym)
    return total_count