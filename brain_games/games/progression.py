from random import randint, choice


def get_answer() -> tuple:
    num1 = randint(1, 20)
    step = randint(1, 20)
    length = randint(5, 10)

    progression = list(map(str, range(num1, num1 + step * length, step)))
    answer = choice(progression)
    progression[progression.index(answer)] = '..'
    question = ' '.join(progression)
    return question, answer
