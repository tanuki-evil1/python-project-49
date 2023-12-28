from random import randint
from text_engine import *


def even_game(name):
    count_correct_answers = 0
    while count_correct_answers < 3:
        num = randint(1, 100)
        answer = 'no' if num % 2 else 'yes'

        question(str(num))
        user_answer = get_user_answer()

        if user_answer == answer:
            correct()
            count_correct_answers += 1
        else:
            wrong_answer(name, user_answer, answer)
            return False
    else:
        congratulations(name)
