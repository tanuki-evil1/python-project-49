from brain_games.scripts.brain_games import welcome_user
from brain_games.games.brain_gcd_game import gcd_game


def main():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    gcd_game(name)


if __name__ == '__main__':
    main()
