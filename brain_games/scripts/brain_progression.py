from brain_games.scripts.brain_games import welcome_user
from brain_games.games.brain_progression_game import progression_game


def main():
    name = welcome_user()
    print("What number is missing in the progression?")
    progression_game(name)


if __name__ == '__main__':
    main()
