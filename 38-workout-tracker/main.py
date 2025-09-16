import json
import os
import requests
from datetime import datetime

APP_ID = os.environ.get("NUTRITIONX_ID")
APP_API = os.environ.get("NUTRITIONX_API")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ.get("SHEETY_ENDPNT")

headers = {
    "Content-Type": 'application/json',
    "x-app-id": APP_ID,
    "x-app-key": APP_API
    }

# usr_input = input("Type your exercise: ")

# params = {
#     "query": usr_input,
#     "gender": "male",
#     "weight_kg": "127",
#     "height_cm": "187"
#     }

# nutritionx_response = requests.post(url=exercise_endpoint, json=params, headers=headers)
# print(nutritionx_response.text)
# data = nutritionx_response.json()
# with open("nutritionx.json", "w") as f:
#     json.dump(data, f, indent=4)

now = datetime.now()
print(now)
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M")
print(date)
print(time)

with open('nutritionx.json', 'r') as f:
    data = json.load(f)

exercise = data['exercises'][0]['user_input']
duration = data['exercises'][0]['duration_min']
calories = data['exercises'][0]['nf_calories']
# print(f"{exercise}, {duration} minutes, {calories} calories burned")

sheet_post = {


# sheety_response = requests.get(url=sheety_endpoint)
# print(sheety_response.text)

post_response = requests.post(url=sheety_endpoint, json=sheet_post)
print(post_response.text)
