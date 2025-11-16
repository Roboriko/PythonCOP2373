# This program deals a 5 card hand using the Deck object as presented
# in Section 11.5. The program uses integers (0-51) that represent the Deck
# of cards. The user is presented with their initial hand of 5 cards and
# the program asks if they would like to exchange any of their cards, if not
# the user may press ENTER on their keyboard and will keep the hand that
# was generated initially.

import random

# Constants
NUM_CARDS_IN_HAND = 5
DECK_SIZE = 52


# Deck Class from section 11.5
class Deck:

    # Creates a shuffled deck of cards
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.cards_in_play_list = []
        self.discards_list = []

    # Shuffles again if the deck is empty
    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print("Reshuffling...!!!")

        # Deals a new card from the top of the deck
        new_card = self.card_list.pop()

        # Keeps track of the cards that are in play
        self.cards_in_play_list.append(new_card)

        return new_card

    # Moves the cards that were in play to the discard pile
    # and clears the cards for new hand of cards
    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()


# Converts the integer card value to ranks and suits
def convert_card_value(card_value):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    rank = ranks[card_value % 13]
    suit = suits[card_value // 13]

    return f"{rank} of {suit}"


# Deals the initial hand of cards
def deal_initial_hand(deck):
    hand = []

    for i in range(NUM_CARDS_IN_HAND):
        hand.append(deck.deal())

    return hand


# Displays the hand of cards to the user
def display_hand(hand):
    print("Your current hand:")

    for index, card in enumerate(hand, start=1):
        print(f"{index}: {convert_card_value(card)}")


# Replaces the card selection done by the user
def draw_new_cards(deck, hand, replace_indices):
    for index in replace_indices:
        hand[index - 1] = deck.deal()

    return hand


# Main function that controls the game
def main():
    # Creates a deck of 52 cards
    deck = Deck(DECK_SIZE)

    # Deals initial hand of cards to the user
    hand = deal_initial_hand(deck)

    # Displays the hand
    display_hand(hand)

    # Asks the user which card they would like to replace, if they would like to
    user_input = input("Please enter a card number you would like to replace (example: 1, 3, 5) or press Enter to keep your initial hand: ")

    # If the user makes a selection then the replacement gets executed
    if user_input.strip():
        replace_indices = [int(num.strip()) for num in user_input.split(',') if num.strip().isdigit()]
        hand = draw_new_cards(deck, hand, replace_indices)

    # Prints on screen the users new hand of cards
    print("Your updated hand:")
    display_hand(hand)

    deck.new_hand()

# Main function that runs program
if __name__ == "__main__":
    main()
