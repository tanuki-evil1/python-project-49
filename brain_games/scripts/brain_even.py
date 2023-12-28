import prompt

from brain_games.scripts.brain_games import main as welcome_user
from random import randint


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_correct_answers = 0
    while count_correct_answers < 3:
        num = randint(1, 100)
        even = 'no' if num % 2 else 'yes'
        print(f'Question: {num}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == even:
            print('Correct!')
            count_correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{even}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
