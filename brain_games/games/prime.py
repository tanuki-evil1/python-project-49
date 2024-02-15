import brain_games.engine_game as engine_game

from random import randint


def is_prime(num: int) -> str:
    if num == 2:
        return 'yes'

    for i in range(3, num):
        if num % i == 0:
            return 'no'
    return 'yes'


def prime_game(name: str) -> None:
    for _ in range(engine_game.CONGRATULATIONS_COUNT):
        num1 = randint(1, 100)
        answer = is_prime(num1)

        engine_game.question(str(num1))
        user_answer = engine_game.get_user_answer()

        if user_answer == answer:
            engine_game.correct()
        else:
            engine_game.wrong_answer(name, user_answer, answer)
            break
    else:
        engine_game.congratulations(name)
