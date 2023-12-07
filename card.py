from colorama import Fore, Back, Style, init
import random

# Initialize colorama for colored console output
init(autoreset=True)

def print_colored(text, color=Fore.WHITE, background_color=Back.BLACK, style=Style.NORMAL):
    """Print colored text to the console."""
    formatted_text = f"{style}{color}{background_color}{text}"
    print(formatted_text)

class Card():
    VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    SUITS = ["Clubs", "Spades", "Diamonds", "Hearts"]

    # Constructor for Card class
    def __init__(self, value, suit):
        """Initialize a card with a given value and suit."""
        self.value = value
        self.suit = suit

    # Class method to create a new shuffled deck
    @classmethod
    def new_deck(cls):
        """Create and shuffle a new deck of cards."""
        deck = [cls(value, suit) for suit in cls.SUITS for value in cls.VALUES]
        random.shuffle(deck)
        return deck

    # String representation of a card
    def __repr__(self):
        """Return a string representation of the card."""
        symbols = {"Clubs": "♣", "Spades": "♠", "Diamonds": "♦", "Hearts": "♥"}
        symbol = symbols.get(self.suit, None)
        if symbol is None:
            raise ValueError("Invalid Suit")

        val_map = {11: "J", 12: "Q", 13: "K", 1: "A"}
        val = val_map.get(self.value, str(self.value))

        return f"{symbol}{val}"

# Calculate the value of a hand considering possible adjustments for aces
def hand_value(hand):
    """Calculate the value of a hand, adjusting for aces if necessary."""
    total = sum(card.value for card in hand)
    num_aces = sum(1 for card in hand if card.value == 1)
    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    return total

# Print the cards in a hand
def print_hand(hand):
    """Print the cards in a given hand."""
    print(" ".join(str(card) for card in hand))

# Blackjack game implementation
def black_jack():
    """Play a game of Blackjack."""
    while True:
        deck = Card.new_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # Check for Blackjack
        if hand_value(player_hand) == 21:
            print("Blackjack! You won!")
        elif hand_value(dealer_hand) == 21:
            print("Dealer has Blackjack. You lost.")
        else:
            while True:
                print(Fore.BLUE + "Your hand:")
                print_hand(player_hand)

                # Human player's move
                add_card = input(Fore.GREEN + "Do you want to add a card? (yes or no): ")
                if add_card.lower() == "yes":
                    player_hand.append(deck.pop())
                    if hand_value(player_hand) > 21:
                        print("Bust! You lost.")
                        break
                else:
                    break

            # Dealer's move
            while hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())

            player_score = hand_value(player_hand)
            dealer_score = hand_value(dealer_hand)

            print("\nYour hand:")
            print_hand(player_hand)
            print("Your score:", player_score)

            print("\nDealer's hand:")
            print_hand(dealer_hand)
            print("Dealer's score:", dealer_score)

            # Determine the winner
            if dealer_score > 21:
                print("Dealer bust! You won.")
            elif player_score > dealer_score:
                print("You won!")
            elif player_score < dealer_score:
                print("You lost.")
            else:
                print("Tie.")

        play_again = input(Fore.RED + "Do you want to play again? (yes or no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing! Goodbye.")
            break

# Start the Blackjack game
black_jack()
