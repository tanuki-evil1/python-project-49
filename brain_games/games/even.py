from random import randint

QUESTION_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_answer() -> tuple:
    num = randint(1, 100)
    return num, 'yes' if num % 2 == 0 else 'no'


def get_data() -> tuple:
    num, answer = get_answer()
    question_exp = str(num)
    return QUESTION_TEXT, question_exp, answer
