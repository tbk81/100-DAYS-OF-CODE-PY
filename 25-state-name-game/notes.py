# with open("weather_data.csv") as f:
#     data = f.readlines()
#     print(data)

import csv

with open("weather_data.csv") as f:
    data = csv.reader(f)
    temperatures = []
    for row in data:
        temperatures.append(row[1])
    print(temperatures)
