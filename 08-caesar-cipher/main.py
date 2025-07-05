from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(direction, usr_text, usr_shift):
    message = ""
    if direction == "decode":
        usr_shift *= -1

    for c in usr_text:
        if c not in alphabet:
            message += c
        else:
            message += alphabet[(alphabet.index(c) + usr_shift) % (len(alphabet))]
    print(f"Here is your {direction}d text: {message}")

done = False
while not done:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, 'e' to exit:\n")
    usr_text = input("Type your message:\n").lower()
    usr_shift = int(input("Type the shift number:\n"))

    caesar(direction, usr_text, usr_shift)
 
    restart = input("Type 'yes' to continue or 'no' to exit\n").lower()
    if restart == "no":
        done = True
        print("Goodbye")