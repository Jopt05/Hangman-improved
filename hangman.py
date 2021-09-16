from typing import Text
from utilities import bcolors, clear, get_word, print_banner
from time import sleep

def script():
    clear()
    word = list( get_word().upper() )
    tries = []
    guesses = []
    print_banner("Welcome to the hangman game")
    while True:
        text = ''
        clear()
        try:
            for char in word:
                if char in guesses:
                    text += f'{char}'
                else:
                    text += "_"
            if text.count("_") == 0:
                print("")
                print(f'{bcolors.OKGREEN}You won with {len(tries)} tries')
                break
            print(text)
            print("")
            print("Introduce your guess:")
            guess_by_user = input("")
            assert len(guess_by_user) == 1, "Only one character by guess"
            assert guess_by_user.isalpha(), "Only letters are allowed"
            guess_by_user = guess_by_user.upper()
            assert guesses.count(guess_by_user) == 0, "You've already tried that!"
            assert tries.count(guess_by_user) == 0, "You've already tried that!"
            if guess_by_user in word:
                guesses.append(guess_by_user)
            else:
                tries.append(guess_by_user)
                print(f'{bcolors.FAIL}Wrong, you"ve tried {len(tries)} times{bcolors.ENDC}')
                sleep(1)
        except AssertionError as ae:
            print(f'{bcolors.WARNING}{ae.args[0]}{bcolors.ENDC}')
            sleep(1)