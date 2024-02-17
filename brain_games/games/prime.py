from random import randint

QUESTION_TEXT = 'Answer "yes" if given number is prime. ' \
                'Otherwise answer "no".'


def is_prime(num: int) -> bool:
    if num == 1:
        return False
    elif num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_answer() -> tuple:
    num = randint(1, 100)
    return num, 'yes' if is_prime(num) else 'no'


def get_data() -> tuple:
    num, answer = get_answer()
    question_exp = str(num)
    return QUESTION_TEXT, question_exp, answer

