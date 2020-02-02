from termcolor import cprint


def choose(name):
    while True:
        print(name + " it's your turn, let's go")
        cprint("Please insert [R] for Rock - OR - [P] for Paper - OR - [S] for Scissors - OR - [L] for Lizard - OR - ["
               "X] for Spock", 'green')
        chosen_move = str(input().lower().strip())
        if chosen_move[0] == "r":
            return 1
            break
        elif chosen_move[0] == "p":
            return 3
            break
        elif chosen_move[0] == "s":
            return 5
            break
        elif chosen_move[0] == "l":
            return 2
            break
        elif chosen_move[0] == "x":
            return 4
            break
        print("Sorry, {0} is not a option, please try again".format(str(chosen_move)))


class RockPaperScissorsLizardSpockGame:
    def __init__(self, player1, player2) -> object:
        self.__round = 1
        print("Hello {0} & hello {1} Welcome to \'Paper, Rock, Scissors, Lizard, Spock\'".format(str(player1.name), str(
            player2.name)))
        print("As Sheldon explains, 'Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons "
              "Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, "
              "Spock vaporizes rock, and as it always has, rock crushes scissors.'")
        print("you will play a best of three - and if there is no winner after that - the tiebreak starts")
        return

    def start_game(self, player1, player2):
        while self.__round <= 3:
            cprint("this is round number: " + str(self.__round), 'green')
            player1.currentHand = choose(player1.name)
            player2.currentHand = choose(player2.name)
            self.evaluate_round(player1, player2)
            print("standings: " + player1.name + " has " + str(player1.score) + " points")
            print("standings: " + player2.name + " has " + str(player2.score) + " points")
            cprint("so its " + str(player1.score) + ":" + str(player2.score) + "  ... what a close call..", 'yellow')
            self.__round += 1
        self.evaluate_game(player1, player2)

    '''  Evaluation Table
    #	Scissors	5	wins against		Paper	    3		Delta   2	    Modulo %5   2
    #	Paper	    3	wins against		rock	    1		Delta   2	    Modulo %5   2
    #	Rock	    1	wins against		scissors	5		Delta   -4	    Modulo %5   1
    #	rock	    1	wins against		lizard	    4		Delta   -3	    Modulo %5   2
    #	lizard	    4	wins against		spock	    2		Delta   2	    Modulo %5   2
    #	spock	    2	wins against		scissors	5		Delta   -3	    Modulo %5   2
    #	scissors	5	wins against		lizard	    4		Delta   1	    Modulo %5   1
    #	lizard	    4	wins against		paper	    3		Delta   1	    Modulo %5   1
    #	paper	    3	wins against		spock	    2		Delta   1	    Modulo %5   1
    #	spock	    2	wins against		rock	    1		Delta   1	    Modulo %5   1
    ##########################################################################################
    #	Paper	    3	loses against		Scissors	5		Delta   -2	    Modulo %5   3
    #	rock	    1	loses against		Paper	    3		Delta   -2	    Modulo %5   3
    #	scissors	5	loses against		Rock	    1		Delta   4	    Modulo %5   4
    #	lizard	    4	loses against		rock	    1		Delta   3	    Modulo %5   3
    #	spock	    2	loses against		lizard	    4		Delta   -2	    Modulo %5   3
    #	scissors	5	loses against		spock	    2		Delta   3	    Modulo %5   3
    #	lizard	    4	loses against		scissors	5		Delta   -1	    Modulo %5   4
    #	paper	    3	loses against		lizard	    4		Delta   -1	    Modulo %5   4
    #	spock	    2	loses against		paper	    3		Delta   -1	    Modulo %5   4
    #	rock	    1	loses against		spock	    2		Delta   -1	    Modulo %5   4'''

    def evaluate_round(self, player1, player2):
        delta = (player1.currentHand - player2.currentHand) % 5
        if delta == 0:
            print("HOLY S%&! ITS A TIE, couldn't get more fun :)")
        elif delta == 1 or delta == 2:
            player1.score += 1
            cprint(
                player1.name + " won this round, because " + player1.return_current_hand() + " beats "
                + player2.return_current_hand() + "!", 'yellow')
        elif delta == 3 or delta == 4:
            player2.score += 1
            cprint(
                player2.name + " won this round, because " + player2.return_current_hand() + " beats "
                + player1.return_current_hand() + "!", 'yellow')
        return

    def evaluate_game(self, player1, player2):
        if player1.score > player2.score:
            cprint(player1.name + " wins the whole game congratulations", 'red')
        elif player2.score > player1.score:
            cprint(player2.name + " wins! the whole game congratulations", 'red')
        elif player2.score == player1.score:
            cprint("Draw after 3 Rounds! TIEBREAK is starting that's a crazy close call... thrilling!", 'red')
            self.start_tiebreak(player1, player2)
        return

    def start_tiebreak(self, player1, player2):
        tiebreak_round_count = 1
        while abs(player1.score - player2.score) < 2:
            cprint("Tiebreak Round Number: " + str(tiebreak_round_count) + " WoW", 'green')
            print("standings: " + player1.name + " has " + str(player1.score) + " points")
            print("standings: " + player2.name + " has " + str(player2.score) + " points")
            player1.currentHand = choose(player1.name)
            player2.currentHand = choose(player2.name)
            self.evaluate_round(player1, player2)
            tiebreak_round_count += 1
        self.evaluate_game(player1, player2)
        return
