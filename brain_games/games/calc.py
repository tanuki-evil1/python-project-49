import operator

from random import randint, choice

QUESTION_TEXT = "What is the result of the expression?"


def get_exp() -> tuple:
    operators = [('+', operator.add), ('*', operator.mul), ('-', operator.sub)]
    num1 = randint(1, 50)
    num2 = randint(1, 10)
    op_text, op = choice(operators)
    return num1, num2, op_text, str(op(num1, num2))


def get_data() -> tuple:
    num1, num2, op_text, answer = get_exp()
    question_exp = f'{num1} {op_text} {num2}'
    return QUESTION_TEXT, question_exp, answer
