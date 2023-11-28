from card import Card
import random

# Blackjack
def black_jack():
    class Player():
        def __init__(self, name, hand, score=0):
            self.name = name
            self.hand = hand
            self.score = score

    class Computer(Player):
        def move(self, pile):
            # TODO: Generate a best possible move
            return None

    class Human(Player):
        def move(self, pile):
            # TODO: Take in a user's input
            return None

    def hand_value(hand):
        total = sum(card.value for card in hand)
        # Handle Ace as 1 or 11
        num_aces = sum(1 for card in hand if card.value == 1)
        while total > 21 and num_aces:
            total -= 10
            num_aces -= 1
        return total

    def print_hand(hand):
        for card in hand:
            print(card)

    deck = Card.new_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("Your hand:")
    print_hand(player_hand)

    # Ask the user if they want to add a card
    add_card = input("Do you want to add a card? (yes or no): ")

    while add_card.lower() == "yes":
        player_hand.append(deck.pop())
        print("Your hand:")
        print_hand(player_hand)
        if hand_value(player_hand) > 21:
            print("Bust! You lost.")
            break
        add_card = input("Do you want to add another card? (yes or no): ")

    player_score = hand_value(player_hand)
    dealer_score = hand_value(dealer_hand)

    print("Your score:", player_score)
    print("Dealer's score:", dealer_score)

    if player_score > 21:
        print("Bust! You lost.")
    elif dealer_score > 21:
        print("Dealer bust! You won.")
    elif player_score > dealer_score:
        print("You won!")
    elif player_score < dealer_score:
        print("You lost.")
    else:
        print("Tie.")

# Game over
black_jack()
