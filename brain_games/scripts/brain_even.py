#!/usr/bin/env python3
from brain_games.scripts.brain_games import welcome
from brain_games.games.even import get_answer
from brain_games.cli import get_user_name
from brain_games.engine_game import game_ready


def main() -> None:
    welcome()
    name = get_user_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_ready(get_answer, name)


if __name__ == '__main__':
    main()
