import random
from art import logo


deck = [11, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 10, 10, 10]
def generate():
    """Generates the deck for start of game"""
    for i in range(2):
        player_deck.append(random.choice(deck))
        comp_deck.append(random.choice(deck))


def hit(hand):
    """Adds cards to deck and checks if you bust with an Ace(11). If so, changed value to 1."""
    c = random.choice(deck)
    hand.append(c)
    if sum(hand) > 21 and hand[-1] == 11:
        hand.pop()
        hand.append(1)


def check_hand(hand):
    """Checks hand to see if player has gone over 21"""
    total = sum(hand)
    if total > 21:
        return True
    return False


def winner(p_hand, c_hand):
    """Compares the two hands to determine who the winner is"""
    p_total = sum(p_hand)
    c_total = sum(c_hand)
    if p_total > c_total or c_total > 21:
        print("You win")
    elif p_total == c_total:
        print("It's a draw!")
    else:
        print("You lose!")


def comp_play(hand):
    while sum(hand) != 0 and sum(hand) < 17:
        hit(hand)


run_game = True
while run_game:
    game_on = input("Do you want to play a game of blackjack? 'y' or 'n': ").lower()
    if game_on == "y":
        print(logo)
        player_deck = []
        comp_deck = []
        generate()
        print(f"Your cards: {player_deck}\nComputer's first card: {comp_deck[0]}\n")
        current_game = True
        while current_game:
            usr_choice = input("Type 'h' to Hit or 'p' to Pass: ").lower()
            if usr_choice == "h":
                hit(player_deck)
                print(f"Your cards: {player_deck}\tTotal = {sum(player_deck)}")
                if check_hand(player_deck):
                    print("Bust! You lose.")
                    print(f"Your final hand: {player_deck}\tTotal = {sum(player_deck)}\nComputer's final hand:"
                          f" {comp_deck}\tTotal = {sum(comp_deck)}")
                    current_game = False
            elif usr_choice == "p":
                comp_play(comp_deck)
                winner(player_deck, comp_deck)
                print(f"Your final hand: {player_deck}\tTotal = {sum(player_deck)}\nComputer's final hand:"
                      f" {comp_deck}\tTotal = {sum(comp_deck)}")
                current_game = False

    else:
        run_game = False
