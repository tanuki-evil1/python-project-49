import prompt

CONGRATULATIONS_COUNT = 3


def congratulations(name: str) -> None:
    print(f'Congratulations, {name}!')


def wrong_answer(name: str, user_answer: str, answer: str) -> None:
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
    print(f"Let's try again, {name}!")


def correct() -> None:
    print('Correct!')


def question(text: str) -> None:
    print(f'Question: {text}')


def get_user_answer() -> str:
    return prompt.string('Your answer: ')


def game_ready(game, name):
    for _ in range(CONGRATULATIONS_COUNT):
        answer = game()
        user_answer = get_user_answer()

        if user_answer == answer:
            correct()
        else:
            wrong_answer(name, user_answer, answer)
            break
    else:
        congratulations(name)
