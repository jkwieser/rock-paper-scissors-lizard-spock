from rnd_game import RNDGame
from player import Player
from rpsls_game import RockPaperScissorsLizardSpockGame


def enter_username():
    while True:
        try:
            username_input = str(input().strip())
            return username_input
            break
        except:
            print("please insert a useful username")


def enter_game_selection():
    while True:
        game_input = str(input()).strip()
        if game_input == '1':
            return game_input
            break
        elif game_input == '2':
            return game_input
            break
        print("Sorry, {0} is not a option, please try again".format(str(game_input)))
        print("Please choose a game")
        print("Press 1 and Enter for 'Random Number Game'")
        print("Press 2 and Enter for 'Rock, Paper, Scissors, Lizard, Spock'")


class MenuStarter:
    def __init__(self) -> object:
        print(
            "Welcome to the first exercise  - it consists of 'Random Number Game' und 'Rock, paper, scissors ("
            "extended with Spock and Lizard) '")
        print("Please enter your nickname")
        player1 = Player(enter_username())
        print("Welcome " + player1.name + " to the first exercise :)")
        print("Select the game you want to play")
        print("Select 1 and Enter for 'Random Number Game'")
        print("Select 2 und Enter für 'Rock, Paper, Scissors, Lizard, Spock'")
        check = enter_game_selection()
        if check == '1':
            print("'Random Number Game' is your selection")
            g = RNDGame(player1.name)
            g.start_game()
        elif check == '2':
            print("'Rock, Paper, Scissors, Lizard, Spock' is your selection")
            print("Please enter name of the second player")
            player2 = Player(enter_username())
            g = RockPaperScissorsLizardSpockGame(player1, player2)
            print("OK let's start the game " + player1.name + " vs. " + player2.name + " have fun")
            g.start_game(player1, player2)
