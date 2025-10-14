import requests
from bs4 import BeautifulSoup
from calendar import Calendar
import os

CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SECRET = os.environ.get("CLIENT_SECRET")

endpoint = "https://www.billboard.com/charts/hot-100/"


def get_weekday(date):
    week_date = ""
    cal = Calendar()
    usr_cal = cal.monthdatescalendar(int(date[0]), int(date[1]))

    for week in range(len(usr_cal)):
        for day in range(len(usr_cal[week])):
            if usr_input == str(usr_cal[week][day]) and usr_input != str(usr_cal[week][-1]):
                week_date = usr_cal[week][-2]
    return week_date


def write_site(site):
    response = requests.get(site)
    with open('website.html', 'w') as file:
        file.write(response.text)


def bb_100_li():
    with open('website.html') as f:
        data = f.read()
    soup = BeautifulSoup(data, 'html.parser')
    song_class = ("c-title a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 "
                  "lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 "
                  "u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025 "
                  "lrv-u-margin-b-00@mobile-max")
    artist_class = ("c-label a-no-trucate a-font-secondary u-font-size-15 "
                    "u-font-size-13@mobile-max u-line-height-18px@mobile-max u-letter-spacing-0010 u-line-height-21px "
                    "a-children-link-color-black a-children-link-color-brand-secondary:hover "
                    "lrv-a-children-link-decoration-underline:hover lrv-u-display-block a-truncate-ellipsis-2line "
                    "u-max-width-397 u-max-width-230@tablet-only u-max-width-300@mobile-max")
    song = soup.find_all(name="h3", class_=song_class)
    artist = soup.find_all(name='span', class_=artist_class)
    hot_100_li = [f"{i + 1}) {artist[i].get_text().strip()} - {song[i].get_text().strip()}" for i in range(len(artist))]
    return hot_100_li


# usr_input = input("Which year do you want to travel to? (YYYY-MM-DD): ")
# usr_date = usr_input.split("-")
#
# travel_week = get_weekday(usr_date)
# write_site(f'{endpoint}/{travel_week}')
bb_100_li()

# ----------------------------------------------- TESTING ----------------------------------------------- #
# Note that the week of billboards start on saturday. i.e., 2000-08-14 would be the week of 08-12 to 8-19
# This would be then usr_cal[1][-2]
# way back archive https://web.archive.org/web/20180219192606/https://www.billboard.com/charts/hot-100/2000-08-26
