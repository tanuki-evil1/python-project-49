import brain_games.engine_game as engine_game

from random import randint


def even_game() -> str:
    num = randint(1, 100)
    answer = 'no' if num % 2 else 'yes'
    engine_game.question(str(num))

    return answer
