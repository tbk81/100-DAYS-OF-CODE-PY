MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '!': '-.-.--', '-': '-....-', '/': '-..-.',
    '(': '-.--.',  ')': '-.--.-'
}

app_on = True
while app_on:
    usr_input = input("Enter your text to translate to Morse Code: ")
    output = []
    if usr_input == "exit":
        app_on = False
    else:
        for char in usr_input.upper():
            if char == " ":
                output.append(" ")
            else:
                output.append(MORSE_CODE_DICT[char])
        print(output)


# if __name__ == "__main__":
#
#     main()





# def text_to_morse(text: str) -> str:
#     morse_output = []
#
#     for char in text.upper():
#         if char == ' ':
#             morse_output.append('/')
#         elif char in MORSE_CODE_DICT:
#             morse_output.append(MORSE_CODE_DICT[char])
#         else:
#             pass
#
#     return ' '.join(morse_output)
#
#
# def main():
#     print("=== TEXT TO MORSE CODE ===")
#     user_input = input("Enter your text: ")
#     morse_result = text_to_morse(user_input)
#     print("\nMorse Code:")
#     print(morse_result)
