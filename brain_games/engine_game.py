import prompt

GAMES_COUNT = 3


def get_user_answer() -> str:
    return prompt.string('Your answer: ')


def run_game(game, name: str) -> None:
    for _ in range(GAMES_COUNT):
        question_text, question_exp, answer = game()
        print(question_text)
        print(f'Question: {question_exp}')
        user_answer = get_user_answer()

        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
