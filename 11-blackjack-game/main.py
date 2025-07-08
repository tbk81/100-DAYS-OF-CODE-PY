import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 10, 10, 10]

player_deck = []
comp_deck = []

# turn this into a function
for i in range(2):
    player_deck.append(random.choice(deck))
    comp_deck.append(random.choice(deck))

print(player_deck)
print(comp_deck)
