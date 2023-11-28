import random
class Card():

    VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    SUITS = ["Clubs", "Spades", "Diamonds", "Hearts"]

    # Constructor
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # New Shuffled Deck Method
    def new_deck(self):
        deck = []
        for suit in Card.SUITS:
            for value in Card.VALUES:
                deck.append(Card(value, suit))
        random.shuffle(deck)
        return deck

    # Print a card as a string
    def __repr__(self):
        # ♣ ♦ ♥ ♠
        if self.suit == "Clubs":
            symbol = "♣"
        elif self.suit == "Spades":
            symbol = "♠"
        elif self.suit == "Diamonds":
            symbol = "♦"
        elif self.suit == "Hearts":
            symbol = "♥"
        else:
            raise Exception("Invalid Suit")

        if self.value == 11: 
            val = "J"
        elif self.value == 12:
            val = "Q"
        elif self.value == 13: 
            val = "K"
        elif self.value == 1: 
            val = "A"
        else: val = self.value

        return f"{symbol}{val}"
        
   
  