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

# new_nums = [n*2 for n in range(1, 5)]
# print(new_nums)

names = ["Beth", "Alex", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
cap_names = [name.upper() for name in names if len(name) > 5]
print(cap_names)

