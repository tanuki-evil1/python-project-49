from brain_games.scripts.brain_games import main as welcome_user
from brain_games.games.brain_calc_game import calc_game


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    calc_game(name )


if __name__ == '__main__':
    main()
