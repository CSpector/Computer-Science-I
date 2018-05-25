# Colton Spector and Quinton Jasper and Peter Giroux
# cbs262 and qjj2 and pag87
# CS126L-003
# Lab10 - Casino Night

import random
# Creation of class Card


class Card:
    def __init__(self, card_num):
        # boolean value that determines face up/down
        self.fdown = True
        # card number variable
        self.card_num = card_num
        # empty string for card suite value
        self.suit = ''
        # division of suits based on card number
        if 0 <= card_num < 13:
            self.suit = "Spade"
        elif 13 <= card_num < 26:
            self.suit = "Hearts"
        elif 26 <= card_num < 39:
            self.suit = "Clubs"
        elif 39 <= card_num < 52:
            self.suit = "Diamonds"
    # simple getter method to retrieve suit

    def get_suit(self):
        return str(self.suit)

    # simple getter method to retrieve card numbers above 10
    def get_rank(self):
        if self.card_num in [0, 13, 26, 39]:
            return "Ace"
        elif self.card_num in [12, 25, 38, 51]:
            return "King"
        elif self.card_num in [11, 24, 37, 50]:
            return "Queen"
        elif self.card_num in [10, 23, 36, 49]:
            return "Jack"
        else:
            return str(self.card_num % 13 + 1)
    # Getter method to retrieve the value of card
    # even if the value is more than 13

    def get_value(self):
        if self.card_num % 13 == 10 or 11 or 12:
            return 10
        elif self.card_num % 13 == 0:
            return 11
        else:
            return str(self.card_num % 13 + 1)

    # Faces cards down
    def face_down(self):
        self.fdown = True

    # faces cards up
    def face_up(self):
        self.fdown = False

    # prints cards suit and rank if faceup
    def __str__(self):
        if self.fdown is False:
            return self.get_rank() + ' of ' + self.get_suit()
        else:
            return "<facedown>"


class ChipBank:
    # sets inputted value in parameter as instance method 'balance'
    def __init__(self, value):
        self.balance = value
    # Withdraws money from our balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance <= 0:
            return 0
        else:
            return amount

    # Adds money into our balance variable
    def deposit(self, amount):
        self.balance = self.balance + amount

    # Simple getter method to retrieve balance amount
    def get_balance(self):
        return self.balance

    # Conducts algorithm to categorize denominations
    # Then prints out the denominations of input
    def __str__(self):
        cash = self.balance
        cash = int(cash * 100)
        a = cash // 10000
        b = (cash - (a*10000)) // 2500
        c = (cash - (a*10000) - (b*2500)) // 500
        d = (cash - (a*10000) - (b*2500) - (c*500)) // 100
        return (str(a) + " Black " + str(b) + " Green " + str(c) + " Red " +
                "and " + str(d) + " Blue. ")

# Run main method only if this is the file ran
if __name__ == "__main__":
    # Lets make a deck of cards
    deck = []
    for i in range(52):
        my_card = Card(i)
        deck.append(my_card)
        # Flip over each card
        my_card.face_up()
        # Print each card as we add them
        print(my_card)
    # Print a random card from the deck
    print(random.choice(deck))
    # in my implementation, card number 37 is the queen of clubs
    card = Card(37)
    print(card)
    # Queen of Clubs
    print(card.get_value())
    # 10
    print(card.get_suit())
    # Clubs
    print(card.get_rank())
    # Queen
    card.face_down()
    print(card)
    # <facedown>
    card.face_up()
    print(card)
    # Queen of Clubs

    cs = ChipBank(149)
    print(cs)
    # 1 blacks, 1 greens, 4 reds, 4 blues - Totaling $149
    cs.deposit(7)
    print(cs.get_balance())
    # 156
    print(cs)
    # 1 blacks, 2 greens, 1 reds, 1 blues - totaling $156
    print(cs.withdraw(84))
    # 84
    print(cs)
    # 0 blacks, 2 greens, 4 reds, 2 blues - totaling $72
    cs.deposit(120)
    print(cs)
    # 1 blacks, 3 greens, 3 reds, 2 blues - totaling 192
    print(cs.withdraw(300))
    # 192
