from random import randint, choice


def get_data() -> tuple:
    question_text = "What number is missing in the progression?"
    num1 = randint(1, 20)
    step = randint(1, 20)
    length = randint(5, 10)

    progression = list(map(str, range(num1, num1 + step * length, step)))
    answer = choice(progression)
    progression[progression.index(answer)] = '..'
    question_exp = question_text + ' '.join(progression)
    return question_text, question_exp, answer
