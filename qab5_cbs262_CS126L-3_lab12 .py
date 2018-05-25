# Colton Spector and Quinn Berry
# cbs262 and qab5
# CS126L-003
# Lab 12 - Blackjack

# Import random so we can shuffle cards in our deck
from random import shuffle
# Import all our classes so we can use relevant methods
from lab10_Answer_Key_MV import Card
from lab10_Answer_Key_MV import ChipBank


# Create a BlackjackHand Class
class BlackjackHand():
    # initialize our deck
    def __init__(self):
        self.hand = []

    # create a method that appends cards to our deck
    def add_card(self, new_card):
        self.hand.append(new_card)

    # Create a way to display the deck to the user
    def __str__(self):
        handString = " "
        count = 1
        for i in self.hand:
            handString += str(i)
            if count != len(self.hand):
                handString += ','
            handString += ' '
            count += 1
        return handString.strip()

    # Get the value of the hand, accounting for the duality of aces
    def get_value(self):
        newValue = 0
        numAce = 0
        for i in self.hand:
            newVar = i
            newValue += newVar.get_value()
            if i.get_value == "Ace":
                numAce += 1
        if newValue > 21:
            if numAce > 0:
                newValue -= 10
                newAce -= 1
        return newValue


# Create a Blackjack class
class Blackjack():

    # Initialize our bank, our deck, and shuffle the deck
    def __init__(self, starting_dollars):
        self.bank = ChipBank(starting_dollars)
        chipStack = str(self.bank)
        self.deck = []
        for i in range(52):
            card = Card(i)
            card.face_up()
            self.deck.append(card)
        shuffle(self.deck)

    # Draw cards and place them into a deck, shuffle if no more cards
    def draw(self):
        if len(self.deck) == 0:
            for i in range(52):
                card = Card(i)
                card.face_up()
                self.deck.append(card)
            shuffle(self.deck)
        drawnCard = self.deck[0]
        del self.deck[0]
        return drawnCard

    # Start the game and give everyone their cards, evaluate win condition
    def start_hand(self, wager):
        self.wager = wager
        self.bank.withdraw(self.wager)
        self.dealerHand = BlackjackHand()
        self.playerHand = BlackjackHand()
        card = self.draw()
        card.face_down()
        self.dealerHand.add_card(card)
        self.dealerHand.add_card(self.draw())
        self.playerHand.add_card(self.draw())
        self.playerHand.add_card(self.draw())
        print("Your starting hand: ", self.playerHand)
        print("Dealers starting hand: ", self.dealerHand)
        if self.playerHand.get_value() == 21:
            if self.dealerHand.get_value() == 21:
                self.end_hand("push")
            else:
                self.end_hand("win")

    # Let the user draw an extra card, evaluate win conditions
    def hit(self):
        self.playerHand.add_card(self.draw())
        print("Your current hand: ", self.playerHand)
        print("Your hands value: ", self.playerHand.get_value())
        if self.playerHand.get_value() > 21:
            self.end_hand("lose")
        elif self.playerHand == 21:
            stand()
            print("21, you stand")

    # Let the user end their turn, make the dealer draw until someone wins,
    # losses or ties
    def stand(self):
        self.dealerHand.hand[0].face_up()
        print("The dealers hand: ", self.dealerHand)
        if self.dealerHand.get_value() >= 16:
            if self.dealerHand.get_value() > self.playerHand.get_value():
                self.end_hand("lose")
            else:
                self.end_hand("win")
        while self.dealerHand.get_value() <= 16:
            self.dealerHand.add_card(self.draw())
            print("The dealers hand: ", self.dealerHand)
        if self.dealerHand.get_value() > 21:
            print("Dealers hand value: ", self.dealerHand.get_value())
            print("The dealer busts!")
            self.end_hand("win")
        elif self.dealerHand.get_value() < 21 and \
                self.playerHand.get_value() < 21:
            if self.dealerHand.get_value() > self.playerHand.get_value():
                print("Dealers hand: ", self.dealerHand.get_value())
                print("Your hand: ", self.playerHand.get_value())
                self.end_hand("lose")
            elif self.dealerHand.get_value() == self.playerHand.get_value():
                print("Dealers hand: ", self.dealerHand.get_value())
                print("Your hand: ", self.playerHand.get_value())
                self.end_hand("push")
            else:
                print("Dealer hand: ", self.dealerHand.get_value())
                print("Your hand: ", self.playerHand.get_value())
                self.end_hand("win")
        if self.playerHand.get_value() == 21:
            self.end_hand("win")

    # Win conditions and messages
    def end_hand(self, outcome):
        self.outcome = outcome
        if self.outcome == "win":
            self.bank.deposit(self.wager*2)
            print("You win!")
        elif self.outcome == "lose":
            print("You lose!")
            pass
        elif self.outcome == "push":
            print("Push, Wager has been returned to you")
            self.bank.deposit(self.wager)
        self.wager = 0
        while len(self.playerHand.hand) > 0:
            del self.playerHand.hand[0]

        while len(self.dealerHand.hand) > 0:
            del self.dealerHand.hand[0]

    # Create a condition to evaluate when the game is running
    def game_active(self):
        if len(self.playerHand.hand) == 0 and len(self.dealerHand.hand) == 0:
            return False
        else:
            return True

# Only run the main method within this file, not from our other classes
if __name__ == "__main__":
    blackjack = Blackjack(250)
    while blackjack.bank.get_balance():
        print("Your remaining chips: "+str(blackjack.bank))
        wager = int(input("How much would you like to wager? "))
        blackjack.start_hand(wager)
        while blackjack.game_active():
            choice = input("STAND or HIT: ").upper()
            if choice == "STAND":
                blackjack.stand()
            elif choice == "HIT":
                blackjack.hit()
        print()
    print("Out of money! The casino wins!")
