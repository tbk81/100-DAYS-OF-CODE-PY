from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
usr_text = input("Type your message:\n").lower()
usr_shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    print(text)
    alphabet.index(shift)


encrypt(usr_text, usr_shift)

# TODO - 1: Create a function called 'encrypt()' that takes 'text' and 'shift' a 2 inputs
# TODO - 2: Inside the 'encrypt()' function, shift each letter of the text forward in the alphabet by the shift amount
#  and print the encrypted text.
# TODO - 3: Call the 'encrypt()' function and pass in the user inputs.
# TODO - 4: What happens when you shift by 9? Can you fix the code?
