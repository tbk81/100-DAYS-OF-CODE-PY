"""Create a letter using starting_letter.txt
for each name in invited_names.txt
Replace the [name] placeholder with the actual name.
Save the letters in the folder "ReadyToSend".
    
Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
"""
name_li = []
with open("Input/Names/invited_names.txt") as f:
    invited_names = f.readlines()
    for name in invited_names:
        strip_name = name.strip()
        name_li.append(strip_name)

with open("Input/Letters/starting_letter.txt") as start_letter:
    new_letter = start_letter.read()


for name in name_li:
    new_letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}_letter.txt", "w") as file:
        file.write(new_letter)
