import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in df.iterrows()}
# print(nato_dict)

while True:
    try:
        usr_input = input("Enter your text: ").upper()
        nato_li = [nato_dict[letter] for letter in usr_input]
    except KeyError:
        print("Type string characters only")
        continue
    else:
        print(nato_li)
    break
