from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, 'e' to exit:\n")
usr_text = input("Type your message:\n").lower()
usr_shift = int(input("Type the shift number:\n"))

def caesar(dir=direction, text=usr_text, shift=usr_shift):
    message = ""

    if dir == "encode":
        print(f"{text}")
        for c in text:
            message += alphabet[(alphabet.index(c) + shift) % (len(alphabet))]
        print(f"Here is your encoded text: {message}")
    elif dir == "decode":
        print(f"{text}")
        for c in text:
            message += alphabet[(alphabet.index(c) - shift) % (len(alphabet))]
        print(f"Here is your decoded text: {message}")
    else:
        print("Please choose encode or decode")

caesar(direction, usr_text, usr_shift)