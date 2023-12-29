from .engine_game import *
from random import randint, choice


def progression_game(name):
    for _ in range(3):
        num1 = randint(1, 20)
        step = randint(1, 20)
        length = randint(5, 10)

        progression = list(map(str, range(num1, num1 + step * length, step)))
        answer = choice(progression)
        progression[progression.index(answer)] = '..'

        question(' '.join(progression))
        user_answer = get_user_answer()

        if user_answer == answer:
            correct()
        else:
            wrong_answer(name, user_answer, answer)
            break
    else:
        congratulations(name)
