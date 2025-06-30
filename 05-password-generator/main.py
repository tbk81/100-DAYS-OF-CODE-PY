import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
in_char = int((input("How many letters would you like in your password?\n")))
in_sym = int((input(f"How many symbols would you like?\n")))
in_num = int((input(f"How many numbers would you like?\n")))

pw = []
for n in range(1, in_char + 1):
    # pw.append(letters[random.randint(1, len(letters) + 1)])
    pw.append(random.choice(letters))

for n in range(1, in_sym + 1):
    pw.append(random.choice(symbols))

for n in range(1, in_num + 1):
    pw.append(random.choice(numbers))

random.shuffle(pw)
pw = "".join(pw)

print(pw)
