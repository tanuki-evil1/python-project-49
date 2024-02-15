import brain_games.engine_game as engine_game

from random import randint, choice


def progression_game() -> str:
    num1 = randint(1, 20)
    step = randint(1, 20)
    length = randint(5, 10)

    progression = list(map(str, range(num1, num1 + step * length, step)))
    answer = choice(progression)
    progression[progression.index(answer)] = '..'

    engine_game.question(' '.join(progression))
    return answer
