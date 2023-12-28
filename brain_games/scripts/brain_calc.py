import operator

import prompt

from brain_games.scripts.brain_games import main as welcome_user
from random import randint, choice


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    count_correct_answers = 0
    operators = [('+', operator.add), ('*', operator.mul), ('-', operator.sub)]
    while count_correct_answers < 3:
        num1 = randint(1, 50)
        num2 = randint(1, 10)
        op_text, op = choice(operators)
        print(f'Question: {num1} {op_text} {num2}')
        user_answer = prompt.string('Your answer: ')
        answer = str(op(num1, num2))
        if user_answer == answer:
            print('Correct!')
            count_correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
