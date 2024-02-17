from random import randint
from math import gcd

QUESTION_TEXT = "Find the greatest common divisor of given numbers."


def get_gcd() -> tuple:
    num1 = randint(1, 50)
    num2 = randint(1, 10)
    return num1, num2, str(gcd(num1, num2))


def get_data() -> tuple:
    num1, num2, answer = get_gcd()
    question_exp = f'{num1} {num2}'
    return QUESTION_TEXT, question_exp, answer
