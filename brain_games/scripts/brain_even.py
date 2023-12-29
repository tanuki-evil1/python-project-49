from brain_games.scripts.brain_games import main as welcome_user
from brain_games.games.brain_even_game import even_game


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    even_game(name)


if __name__ == '__main__':
    main()
