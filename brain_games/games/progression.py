from random import randint, choice


def get_progression() -> tuple:
    num = randint(1, 20)
    step = randint(1, 20)
    length = randint(5, 10)
    progression = list(map(str, range(num, num + step * length, step)))
    return progression, choice(progression)


def get_data() -> tuple:
    question_text = "What number is missing in the progression?"

    progression, answer = get_progression()
    progression[progression.index(answer)] = '..'
    question_exp = ' '.join(progression)
    return question_text, question_exp, answer
