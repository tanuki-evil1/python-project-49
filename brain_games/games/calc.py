import operator
import brain_games.engine_game as engine_game

from random import randint, choice


def calc_game() -> str:
    operators = [('+', operator.add), ('*', operator.mul), ('-', operator.sub)]

    num1 = randint(1, 50)
    num2 = randint(1, 10)
    op_text, op = choice(operators)
    answer = str(op(num1, num2))

    engine_game.question(f'{num1} {op_text} {num2}')
    return answer
