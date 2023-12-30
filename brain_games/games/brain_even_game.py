import brain_games.games.engine_game as engine_game

from random import randint


def even_game(name):
    for _ in range(3):
        num = randint(1, 100)
        answer = 'no' if num % 2 else 'yes'

        engine_game.question(str(num))
        user_answer = engine_game.get_user_answer()

        if user_answer == answer:
            engine_game.correct()
        else:
            engine_game.wrong_answer(name, user_answer, answer)
            return False
    else:
        engine_game.congratulations(name)
