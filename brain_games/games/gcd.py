import brain_games.engine_game as engine_game

from random import randint
from math import gcd


def gcd_game() -> str:
    num1 = randint(1, 50)
    num2 = randint(1, 10)

    answer = str(gcd(num1, num2))

    engine_game.question(f'{num1} {num2}')
    return answer
