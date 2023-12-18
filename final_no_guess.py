# assign number

import random

game_no = random.randint(1, 100)

# ask user to guess the number and difficult level

difficulty = input('''Welcome to the guessing game! \n
Choose a difficulty level -- easy or hard:''')


def check_level(level):
    if level == 'easy':
        tries = 10
        return tries
    elif level == 'hard':
        tries = 5
        return tries


# ask user to guess till he has guesses left
def play_game():
    n_guesses = check_level(difficulty)
    # print(n_guesses)
    while n_guesses > 0:
        guess_no = int(input("Guess a number between 1 and 100:"))
        if guess_no == game_no:
            print("You have won")
            break
        elif guess_no > game_no:
            print("Too high")
        elif guess_no < game_no:
            print("Too low")
        n_guesses -= 1

    if n_guesses == 0:
        print(f"You have lost!\n The number was {game_no}\nDo you want to play again?")
        if input("Y/N: ") == 'Y':
            play_game()
        else:
            print("Thanks")


play_game()
