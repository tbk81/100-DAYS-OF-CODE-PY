# Handling errors
# try - somethign that might cause an exception
# except - Do this if there was an exception (if somthing went wrong, do this)
# else - Do this if there were no exceptions (error)
# finally - Do this no matter what happens

# FileNotFoundError
# try:
#     file = open('a_file.txt')
#     a_dict = {"key": "value"}
#     print(a_dict["not here"])
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write("somthing was written")
# except KeyError as error_message:
#     print(f'Key {error_message} does not exist')
# else:
#     content = file.read()
#     print(content)
# finally:
    # file.close()
    # print("File was closed")

height = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))

if height > 3:
    raise ValueError("Height should not be greater than 3 meters")

bmi = weight / height ** 2
print(bmi)


try:
    pass
except In: