import operator
import brain_games.engine_game as engine_game

from random import randint, choice


def calc_game(name: str) -> None:
    operators = [('+', operator.add), ('*', operator.mul), ('-', operator.sub)]

    for _ in range(engine_game.CONGRATULATIONS_COUNT):
        num1 = randint(1, 50)
        num2 = randint(1, 10)
        op_text, op = choice(operators)
        answer = str(op(num1, num2))

        engine_game.question(f'{num1} {op_text} {num2}')
        user_answer = engine_game.get_user_answer()

        if user_answer == answer:
            engine_game.correct()
        else:
            engine_game.wrong_answer(name, user_answer, answer)
            break
    else:
        engine_game.congratulations(name)
