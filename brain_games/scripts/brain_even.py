#!/usr/bin/env python3
from brain_games.scripts.brain_games import welcome
from brain_games.games.brain_even_game import even_game
from brain_games.cli import get_user_name


def main() -> None:
    welcome()
    name = get_user_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    even_game(name)


if __name__ == '__main__':
    main()
