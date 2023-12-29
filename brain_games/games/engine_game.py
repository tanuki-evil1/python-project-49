import prompt


def congratulations(name: str):
    print(f'Congratulations, {name}!')


def wrong_answer(name: str, user_answer: str, answer: str):
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
    print(f"Let's try again, {name}!")


def correct():
    print('Correct!')


def question(text: str):
    print(f'Question: {text}')


def get_user_answer():
    return prompt.string('Your answer: ')
