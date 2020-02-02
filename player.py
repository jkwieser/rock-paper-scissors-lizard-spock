class Player:
    def __init__(self, name) -> object:
        self.name = name
        self.score = 0
        self.currentHand = 0
        return

    def return_current_hand(self):
        if self.currentHand == 1:
            return "Rock"
        elif self.currentHand == 3:
            return "Paper"
        elif self.currentHand == 5:
            return "Scissors"
        elif self.currentHand == 2:
            return "Spock"
        elif self.currentHand == 4:
            return "Lizard"
