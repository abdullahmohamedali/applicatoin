import random

# Card deck creation: Each card is represented as a tuple (value, suit)
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
}

# Create the deck
deck = [(value, suit) for value in values for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Deal cards to two players
player1_hand = deck[:26]
player2_hand = deck[26:]

# Game logic
print("Starting the game of War!\n")
round_number = 1

while player1_hand and player2_hand:
    print(f"--- Round {round_number} ---")
    # Each player draws the top card
    card1 = player1_hand.pop(0)
    card2 = player2_hand.pop(0)
    
    # Display the cards
    print(f"Player 1 plays: {card1[0]} of {card1[1]}")
    print(f"Player 2 plays: {card2[0]} of {card2[1]}")

    # Compare cards
    if values[card1[0]] > values[card2[0]]:
        print("Player 1 wins this round!\n")
        player1_hand.extend([card1, card2])
    elif values[card1[0]] < values[card2[0]]:
        print("Player 2 wins this round!\n")
        player2_hand.extend([card1, card2])
    else:
        print("It's a tie! Cards are discarded.\n")

    round_number += 1

    # Pause for the player
    input("Press Enter to continue...")

# Determine the winner
if player1_hand:
    print("Player 1 wins the game!")
else:
    print("Player 2 wins the game!")
