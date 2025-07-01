import random, string

word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
for c in chosen_word:
    placeholder += "_"
print(placeholder)

# TODO-1 - Create a while loop that will let the user guess again

game_over = False
while not game_over:

    guess = input("Choose a letter: ").lower()
    display = ""

# TODO-2 - Change the for loop so that you keep the previous correct letters in the display.

    for l in chosen_word:
        if guess == l:
            display += l
            # print("right")
        else:
            display += "_"
            # print("wrong")
    print(display)