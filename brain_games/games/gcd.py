from random import randint
from math import gcd


def get_answer() -> tuple:
    num1 = randint(1, 50)
    num2 = randint(1, 10)
    answer = str(gcd(num1, num2))
    question = f'{num1} {num2}'
    return question, answer
