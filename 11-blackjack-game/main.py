import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 10, 10, 10]


def hit(cards):
    '''Adds cards to deck and checks if you bust with an Ace(11). If so, changed value to 1.'''
    c = random.choice(deck)
    cards.append(c)
    if sum(cards) > 21 and cards[-1] == 11:
        cards.pop()
        cards.append(1)


def generate():
    '''Generates the deck for start of game'''
    for i in range(2):
        player_deck.append(random.choice(deck))
        comp_deck.append(random.choice(deck))

run_game = True
while run_game:
    game_on = input("Do you want to play a game of blackjack? 'y' or 'n': " ).lower()
    if game_on == "y":
        player_deck = []
        comp_deck = []
        generate()
        print(f"Your cards: {player_deck}\nComputer's first cards: {comp_deck[0]}\n")
        if sum(player_deck) < 22:
            usr_choice = input("Type 'h' to Hit or 'p' to Pass: ").lower()
            if usr_choice == "h":
                hit(player_deck)
                print(player_deck)
    else:
        run_game = False
