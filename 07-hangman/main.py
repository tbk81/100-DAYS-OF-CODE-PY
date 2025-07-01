import random
from art import stages, logo
from words import word_list

total_lives = 6
lives = 6

print(logo)
chosen_word = random.choice(word_list)
# print(chosen_word)
placeholder = ""
for c in chosen_word:
    placeholder += "_"
print(f"Word to guess: {placeholder}")
print(f"************** {lives}/{total_lives} LIVES LEFT **************")

game_over = False
correct_letters = []

while not game_over:
    guess = input("Choose a letter: ").lower()
    display = ""

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word. You lose a life.")
        if lives == 0:
            print(f"You lose. The word was {chosen_word}")
            game_over = True

    print(f"Word to guess: {display}")
    print(f"************** {lives}/{total_lives} LIVES LEFT **************")

    if "_" not in display:
        print("You win!")
        game_over = True

    print(stages[lives])
