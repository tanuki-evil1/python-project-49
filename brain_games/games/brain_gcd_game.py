from .text_engine import *
from random import randint
from math import gcd


def gcd_game(name):
    count_correct_answers = 0
    while count_correct_answers < 3:
        num1 = randint(1, 50)
        num2 = randint(1, 10)

        answer = str(gcd(num1, num2))

        question(f'{num1} {num2}')
        user_answer = get_user_answer()

        if user_answer == answer:
            correct()
            count_correct_answers += 1
        else:
            wrong_answer(name, user_answer, answer)
            break
    else:
        congratulations(name)
