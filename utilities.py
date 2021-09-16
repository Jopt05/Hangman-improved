from os import system
import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Cleans the console 
def clear():
    system("clear")

# Gets the word from the API
def get_word():
    response = requests.get("https://palabras-aleatorias-public-api.herokuapp.com/random").json()
    word = response["body"]["Word"]
    return word

def print_banner(text):
    print(f'{bcolors.HEADER}------------------------{bcolors.ENDC}')
    print(f'{bcolors.HEADER}{text}{bcolors.ENDC}')
    print(f'{bcolors.HEADER}------------------------{bcolors.ENDC}')