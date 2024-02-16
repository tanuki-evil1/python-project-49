from random import randint


def is_even(num: int) -> bool:
    return num % 2 == 0


def get_data() -> tuple:
    question_text = 'Answer "yes" if the number is even, otherwise answer "no".'
    num = randint(1, 100)
    answer = 'yes' if is_even(num) else 'no'
    question_exp = str(num)
    return question_text, question_exp, answer
