import requests
from bs4 import BeautifulSoup
from calendar import Calendar
import os

CLIENT_ID = "SPOTIFY_CLIENT_ID"
SECRET = "CLIENT_SECRET"

usr_input = input("Which year do you want to travel to? (YYYY-MM-DD): ")
usr_date = usr_input.split("-")


def get_weekday(date):
    week_date = ""
    cal = Calendar()
    usr_cal = cal.monthdatescalendar(int(date[0]), int(date[1]))

    for week in range(len(usr_cal)):
        for day in range(len(usr_cal[week])):
            if usr_input == str(usr_cal[week][day]) and usr_input != str(usr_cal[week][-1]):
                week_date = usr_cal[week][-2]
    return week_date

        # print(usr_cal[week][day])
    # if str(usr_cal[week][day]) == usr_input:
    #     print(usr_cal[week])
    # print(usr_cal[week][day])
# print(usr_cal[1][-2])




# ----------------------------------------------- TESTING ----------------------------------------------- #
# Note that the week of billboards start on saturday. i.e., 2000-08-14 would be the week of 08-12 to 8-19
# This would be then usr_cal[1][-2]
# way back archive https://web.archive.org/web/20180219192606/https://www.billboard.com/charts/hot-100/2000-08-26


