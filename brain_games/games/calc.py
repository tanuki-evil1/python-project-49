import operator

from random import randint, choice

QUESTION_TEXT = "What is the result of the expression?"

<<<<<<< Updated upstream
def get_exp(num1, num2):
    operators = [('+', operator.add), ('*', operator.mul), ('-', operator.sub)]
    op_text, op = choice(operators)
    return op_text, str(op(num1, num2))


def get_data() -> tuple:
    question_text = "What is the result of the expression?"
    num1 = randint(1, 50)
    num2 = randint(1, 10)

    op_text, answer = get_exp(num1, num2)
=======

def get_exp() -> tuple:
    operators = [('+', operator.add), ('*', operator.mul), ('-', operator.sub)]
    num1 = randint(1, 50)
    num2 = randint(1, 10)
    op_text, op = choice(operators)
    return num1, num2, op_text, str(op(num1, num2))


def get_data() -> tuple:
    num1, num2, op_text, answer = get_exp()
>>>>>>> Stashed changes
    question_exp = f'{num1} {op_text} {num2}'
    return QUESTION_TEXT, question_exp, answer
