from random import randint
from .engine_game import *


def even_game(name):
    for _ in range(3):
        num = randint(1, 100)
        answer = 'no' if num % 2 else 'yes'

        question(str(num))
        user_answer = get_user_answer()

        if user_answer == answer:
            correct()
        else:
            wrong_answer(name, user_answer, answer)
            return False
    else:
        congratulations(name)
