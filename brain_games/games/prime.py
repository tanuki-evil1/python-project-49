from random import randint


def is_prime(num: int) -> bool:
    if num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_answer() -> tuple:
    num1 = randint(1, 100)
    answer = 'yes' if is_prime(num1) else 'no'
    question = str(num1)
    return question, answer
