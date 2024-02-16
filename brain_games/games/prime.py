from random import randint


def is_prime(num: int) -> bool:
    if num == 1:
        return False
    elif num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_data() -> tuple:
    question_text = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    num1 = randint(1, 100)
    answer = 'yes' if is_prime(num1) else 'no'
    question = question_text + str(num1)
    return question, answer
