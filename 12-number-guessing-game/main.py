import random

EASY = 10
HARD = 5

print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
num_to_guess = random.randint(1, 100)
print(num_to_guess)
usr_choice = input("Choose a difficulty. Type 'e' for easy and 'h' for hard: ")
if usr_choice == "e":
    guesses_left = EASY
else:
    guesses_left = HARD

play_game = True
while play_game:
    print(f"You have {guesses_left} attempts remaining to guess the number")
    current_guess = int(input("Make a guess: "))
    if current_guess > num_to_guess:
        print("Too high")
        guesses_left -= 1
    elif current_guess < num_to_guess:
        print("Too low")
        guesses_left -= 1
    elif current_guess == num_to_guess:
        print("You guessed correctly!")
        play_game = False

    if guesses_left == 0:
        print(f"You ran out of guesses! The number was {num_to_guess}")
        play_game = False
