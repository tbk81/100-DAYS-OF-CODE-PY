from art import logo

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

def morse_code_translate(text):
    output = []
    for char in text.upper():
        if char == " ":
            output.append(" ")
        else:
            output.append(MORSE_CODE_DICT[char])
    return ' '.join(output)

def main():
    print(logo)
    app_on = True
    while app_on:
        usr_input = input("Enter your text to translate to Morse Code: ")
        if usr_input == "exit":
            app_on = False
        else:
            result = morse_code_translate(usr_input)
            print(result)


if __name__ == "__main__":
    main()
