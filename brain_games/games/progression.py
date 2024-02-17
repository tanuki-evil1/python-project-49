from random import randint, choice

QUESTION_TEXT = "What number is missing in the progression?"


def get_progression() -> tuple:
    num = randint(1, 20)
    step = randint(1, 20)
    length = randint(5, 10)
    progression = list(map(str, range(num, num + step * length, step)))
    return progression, choice(progression)


def get_data() -> tuple:
    progression, answer = get_progression()
    progression[progression.index(answer)] = '..'
    question_exp = ' '.join(progression)
    return QUESTION_TEXT, question_exp, answer
