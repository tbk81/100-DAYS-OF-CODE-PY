import random
from turtledemo.sorting_animate import enable_keys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
names = ["ROCK", "PAPER", "SCISSORS"]
hands = [rock, paper, scissors]

print("Let's play rock paper scissors!")
usr_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n"))
comp_choice = random.randint(0, 2)

print("You chose:\n" + names[usr_choice] + "\n" + hands[usr_choice])
print("Computer chose:\n" + names[comp_choice] + "\n" + hands[comp_choice])

if usr_choice == 0 and comp_choice == 1:
    print("You lose!")
elif usr_choice == 0 and comp_choice == 2:
    print("You win!")
elif usr_choice == 1 and comp_choice == 0:
    print("You win!")
elif usr_choice == 1 and comp_choice == 2:
    print("You lose!")
elif usr_choice == 2 and comp_choice == 0:
    print("You lose!")
elif usr_choice == 2 and comp_choice == 1:
    print("You win!")
else:
    print("Draw!")
