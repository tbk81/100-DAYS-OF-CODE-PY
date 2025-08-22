import requests
from datetime import datetime
import time

MY_LAT = 34.052235
MY_LNG = -118.243683
TZID = "America/Los_Angeles"
SUN_URL = "https://api.sunrise-sunset.org/json"
ISS_URL = "http://api.open-notify.org/iss-now.json"
my_email = "tbk81dev@gmail.com"
password = "dnchhnyasyhcqwfb"


def is_night():
    params = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
        "tzid": TZID,
    }

    response = requests.get(url=SUN_URL, params=params)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_hour = datetime.now().hour
    if current_hour >= sunset or current_hour <= sunrise:
        return True
    else:
        return False


def iss_overhead():
    response = requests.get(url=ISS_URL)
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LNG - 5) < iss_longitude < (MY_LNG + 5):
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_night() and iss_overhead():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject: ISS is overhead👆\n\nLook up in the sky, the ISS is overhead!"
                                )
