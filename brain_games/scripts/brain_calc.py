#!/usr/bin/env python3
from brain_games.scripts.brain_games import welcome
from brain_games.cli import get_user_name
from brain_games.games.calc import get_answer
from brain_games.engine_game import game_ready


def main() -> None:
    welcome()
    name = get_user_name()
    print('What is the result of the expression?')
    game_ready(get_answer, name)


if __name__ == '__main__':
    main()
