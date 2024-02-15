import brain_games.engine_game as engine_game

from random import randint


def is_prime(num: int) -> str:
    if num == 2:
        return 'yes'

    for i in range(2, num):
        if num % i == 0:
            return 'no'
    return 'yes'


def prime_game() -> str:
    num1 = randint(1, 100)
    answer = is_prime(num1)

    engine_game.question(str(num1))
    return answer
