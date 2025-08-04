# list comprehension
# new_list = [new_item for item in list]
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)
#
# new_list = [n+1 for n in numbers]
# print(new_list)
from os import pathconf_names

# new_nums = [n*2 for n in range(1, 5)]
# print(new_nums)

# names = ["Beth", "Alex", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
# cap_names = [name.upper() for name in names if len(name) > 5]
# print(cap_names)

# Dictionary Comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)
#
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {word: (temp * 9 / 5) + 32 for word, temp in weather_c.items()}
# print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# loop through dictionary
# for key, value in student_dict.items():
#     print(key, value)

import pandas

student_df = pandas.DataFrame(student_dict)
print(student_df)

# loop through dataframe
# for k,v in student_df.items():
    # print(k)
    # print(v)

# loop through the rows
for index,row in student_df.iterrows():
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)





