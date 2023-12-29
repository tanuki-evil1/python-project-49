import operator

from .engine_game import *
from random import randint, choice


def calc_game(name):
    operators = [('+', operator.add), ('*', operator.mul), ('-', operator.sub)]

    for _ in range(3):
        num1 = randint(1, 50)
        num2 = randint(1, 10)
        op_text, op = choice(operators)
        answer = str(op(num1, num2))

        question(f'{num1} {op_text} {num2}')
        user_answer = get_user_answer()

        if user_answer == answer:
            correct()
        else:
            wrong_answer(name, user_answer, answer)
            break
    else:
        congratulations(name)
