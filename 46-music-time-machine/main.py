import requests
from bs4 import BeautifulSoup
from calendar import Calendar

# usr_input = input("Which year do you want to travel to? (YYYY-MM-DD): ")
usr_input = "2000-08-14"
usr_date = usr_input.split("-")

# print(usr_input)
# print(usr_date)
cal = Calendar()
# print(cal.monthdays2calendar(int(usr_date[0]), int(usr_date[1])))
# usr_cal = cal.monthdays2calendar(int(usr_date[0]), int(usr_date[1]))
usr_cal = cal.monthdatescalendar(int(usr_date[0]), int(usr_date[1]))
for week in range(len(usr_cal)):
    # print(usr_cal[week])
    print(usr_cal[week][-2])
    # for day in range(len(usr_cal[week])):
    #     if str(usr_cal[week][day]) == usr_input:
    #         print(usr_cal[week])
        # print(usr_cal[week][day])
# print(usr_cal[1][-2])


# Note that the week of billboards start on saturday. i.e., 2000-08-14 would be the week of 08-12 to 8-19
# This would be then usr_cal[1][-2]
# way back archive https://web.archive.org/web/20180219192606/https://www.billboard.com/charts/hot-100/2000-08-26


