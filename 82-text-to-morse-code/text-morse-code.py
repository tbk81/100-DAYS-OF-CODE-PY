from art import logo
from morse_code_dict import MORSE_CODE_DICT

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
