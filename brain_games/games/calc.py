import operator

from random import randint, choice


def get_data() -> tuple:
    question_text = "What is the result of the expression?"
    operators = [('+', operator.add), ('*', operator.mul), ('-', operator.sub)]
    num1 = randint(1, 50)
    num2 = randint(1, 10)
    op_text, op = choice(operators)
    answer = str(op(num1, num2))
    question_exp = f'{num1} {op_text} {num2}'
    return question_text, question_exp, answer
