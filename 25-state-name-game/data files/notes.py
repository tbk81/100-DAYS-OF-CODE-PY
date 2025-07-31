# with open("weather_data.csv") as f:
#     data = f.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# temp_li = data["temp"].tolist()
# average = sum(temp_li) / len(temp_li)
# print(f"{average:.2f}")
# print(data["temp"].mean())
# print(data.temp.mean())
# print(data["temp"].max())
#
# Get data in columns
# print(data.condition)
# print(data.temp)

# Get data in a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp)
#
# far = monday.temp * (9/5) + 32
# print(far)
# print(type(far))
#
# monday_temp = monday.temp[0]
# far_2 = monday_temp * (9/5) + 32
# print(far_2)
# print(type(far_2))


# Create a new dataframe
# data_dict = {
#     "students": ["Amy", "James", "Zora"],
#     "scores": [81, 73, 91],
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data_file")

# Using the squirrel data make a dataframe with the number of squirrels by number
sq_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = sq_data["Primary Fur Color"].tolist()
# print(colors)
sq_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [colors.count("Gray"), colors.count("Cinnamon"),  colors.count("Black")]
}

# print(sq_dict)

df = pandas.DataFrame(sq_dict)
df.to_csv("squirrel color count")

