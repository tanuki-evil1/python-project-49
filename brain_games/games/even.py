from random import randint


def is_even(num: int) -> bool:
    return num % 2 == 0


def get_answer() -> tuple:
    num = randint(1, 100)
    answer = 'yes' if is_even(num) else 'no'
    question = str(num)
    return question, answer
