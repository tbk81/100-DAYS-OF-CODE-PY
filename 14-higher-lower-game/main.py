import random
from art import logo, vs
from game_data import data


def compare(answer):
    if answer == "a" and personA['follower_count'] > personB['follower_count']:
        return True
    elif answer == "b" and personA['follower_count'] < personB['follower_count']:
        return True
    else:
        return False


def person_gen():
    return data[random.randint(0, len(data) - 1)]


personA = person_gen()
personB = person_gen()

current_score = 0
game_running = True
while game_running:
    if personA == personB:
        personB = person_gen()

    print(logo)
    print(f"Compare A: {personA['name']}, a {personA['description']} from {personA['country']}")
    print(vs)
    print(f"Compare B: {personB['name']}, a {personB['description']} from {personB['country']}")
    # print(f"A = {personA['follower_count']}\nB = {personB['follower_count']}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if compare(user_choice):
        current_score += 1
        print(f"Correct! Your current score is: {current_score}")
        if user_choice == "a":
            personB = person_gen()
        else:
            personA = personB
    else:
        print(f"Incorrect. Game over. Your final score is {current_score}")
        game_running = False
