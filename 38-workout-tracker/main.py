import json
import os
import requests
from datetime import datetime

APP_ID = os.environ.get("NUTRITIONX_ID")
APP_API = os.environ.get("NUTRITIONX_API")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ.get("SHEETY_ENDPNT")

nutritionx_headers = {
    "Content-Type": 'application/json',
    "x-app-id": APP_ID,
    "x-app-key": APP_API
    }

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

usr_input = input("Type your exercise: ")

params = {
    "query": usr_input,
    "gender": "male",
    "weight_kg": "127",
    "height_cm": "187"
    }

nutritionx_response = requests.post(url=exercise_endpoint, json=params, headers=nutritionx_headers)
result = nutritionx_response.json()
# print(nutritionx_response.text)
# data = nutritionx_response.json()
# with open("nutritionx.json", "w") as f:
#     json.dump(data, f, indent=4)

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M")

# with open('nutritionx.json', 'r') as f:
#     data = json.load(f)

# exercise = data['exercises'][0]['user_input']
# duration = data['exercises'][0]['duration_min']
# calories = data['exercises'][0]['nf_calories']

for exercise in result['exercises']:
    sheet_post = {
        "workout": {
            "Date": date,
            "Time": time,
            "Exercise": exercise['name'].title(),
            "Duration": exercise['duration_min'],
            "Calories": exercise['nf_calories']
            }
        }
    post_response = requests.post(sheety_endpoint, json=sheet_post, headers=sheety_headers)
    print(post_response.text)

# sheety_response = requests.get(url=sheety_endpoint)
# print(sheety_response.text)

