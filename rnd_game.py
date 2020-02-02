from random import randrange
from termcolor import cprint


class RNDGame():

    def __init__(self, username) -> object:
        self.username = username
        print("Hallo " + self.username + " Welcome to 'Random Number Game'")
        print("The goal of the game is that you correctly guess a random number from 1-25. You have 5 rounds to win "
              "the game! Otherwise you lose. Let's go")
        print("")
        self.__random_number = randrange(1, 26, 1)
        self.__round = 1
        return

    def start_game(self):
        while self.__round <= 5:
            print("this is round number: " + str(self.__round))
            print("waiting for your guess.... :)")
            my_guess = self.guess()
            if self.__random_number == my_guess:
                return self.game_won()

            elif self.__random_number > my_guess:
                print("Hint: the secret number you are looking for is higher than your input")
            elif self.__random_number < my_guess:
                print("Hint: the secret number you are looking for is lower than your input")
            self.__round += 1
        self.game_lost()

    def guess(self):
        while True:
            try:
                guess_number = int(input())
                return guess_number
                break
            except:
                print("please insert only numbers")

    def game_won(self):
        cprint("you won, awesome", 'green')

    def game_lost(self):
        cprint("you lost because 5 rounds are over, I'm soo sorry :(", 'red')
