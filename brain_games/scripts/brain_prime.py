#!/usr/bin/env python3
from brain_games.scripts.brain_games import welcome
from brain_games.games.brain_prime_game import prime_game
from brain_games.cli import get_user_name


def main():
    welcome()
    name = get_user_name()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    prime_game(name)


if __name__ == '__main__':
    main()
