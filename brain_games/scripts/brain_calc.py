#!/usr/bin/env python3
from brain_games.scripts.brain_games import welcome
from brain_games.cli import get_user_name
from brain_games.games.calc import get_data
from brain_games.engine_game import run_game


def main() -> None:
    welcome()
    name = get_user_name()
    run_game(get_data, name)


if __name__ == '__main__':
    main()
