# file = open("24-auto-letter-addressor/my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Read a file - To get rid of the file.close() and automatically close the file
# defualt mode is read only

# with open("24-auto-letter-addressor/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Write a file - mode w rewrites the file, mode a appends to the file
# Opening a file from write mode will create the file if it does not exist
# with open("24-auto-letter-addressor/my_file.txt", mode="a") as file:
#     file.write("\nI'm writing to this file")

with open("new_file.txt", mode="w") as file:
    file.write("This is a new file with new text")