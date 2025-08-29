import requests
import os

API = os.environ.get("OWM_API_KEY")
URL = "https://api.openweathermap.org/data/2.5/forecast"
# LAT = 32.715736
# LON = -117.161087
LAT = 34.748741
LON = -92.275101

params = {
    "lat": LAT,
    "lon": LON,
    "cnt": 4,
    "appid": API
}

response = requests.get(url=URL, params=params)
print(response.status_code)
response.raise_for_status()
data = response.json()
# print(data)
rain = False
for w in data["list"]:
    code = w["weather"][0]["id"]
    if int(code) < 700:
        rain = True
        # print(data["list"][w]["weather"][0]["description"])
        # print(data["list"][w]["dt_txt"] + "\n")
if rain:
    print("Bring an umbrella!")


