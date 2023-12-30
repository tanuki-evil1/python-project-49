#!/usr/bin/env python3
from brain_games.scripts.brain_games import welcome
from brain_games.games.brain_gcd_game import gcd_game
from brain_games.cli import get_user_name


def main() -> None:
    welcome()
    name = get_user_name()
    print("Find the greatest common divisor of given numbers.")
    gcd_game(name)


if __name__ == '__main__':
    main()
