import requests

API = "5122bf76ae7d608296508c588859cfde"
URL = "https://api.openweathermap.org/data/2.5/forecast"
LAT = 32.715736
LON = -117.161087

params = {
    "lat": LAT,
    "lon": LON,
    "appid": API
}

response = requests.get(url=URL, params=params)
print(response.status_code)
response.raise_for_status()
data = response.json()
# print(data)
for w in range(len(data["list"])):
    print(data["list"][w]["weather"][0]["description"])
    print(data["list"][w]["dt_txt"] + "\n")


