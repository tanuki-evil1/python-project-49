import brain_games.games.engine_game as engine_game

from random import randint, choice


def progression_game(name):
    for _ in range(3):
        num1 = randint(1, 20)
        step = randint(1, 20)
        length = randint(5, 10)

        progression = list(map(str, range(num1, num1 + step * length, step)))
        answer = choice(progression)
        progression[progression.index(answer)] = '..'

        engine_game.question(' '.join(progression))
        user_answer = engine_game.get_user_answer()

        if user_answer == answer:
            engine_game.correct()
        else:
            engine_game.wrong_answer(name, user_answer, answer)
            break
    else:
        engine_game.congratulations(name)
