from random import randint
from math import gcd


def get_data() -> tuple:
    question_text = "Find the greatest common divisor of given numbers.\n"
    num1 = randint(1, 50)
    num2 = randint(1, 10)
    answer = str(gcd(num1, num2))
    question = question_text + f'{num1} {num2}'
    return question, answer
