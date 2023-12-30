import brain_games.games.engine_game as engine_game

from random import randint


def is_prime(num):
    if num == 2:
        return 'yes'

    for i in range(3, num):
        if num % i == 0:
            return 'no'
    return 'yes'


def prime_game(name):
    for _ in range(3):
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
