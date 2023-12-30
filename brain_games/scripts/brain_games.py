#!/usr/bin/env python3
from brain_games.cli import get_user_name


def welcome() -> None:
    print("Welcome to the Brain Games!")


def main() -> None:
    welcome()
    get_user_name()


if __name__ == '__main__':
    main()
