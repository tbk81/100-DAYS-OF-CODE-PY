import os
import requests

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

sheety_response = requests.get(url=sheety_endpoint)
print(sheety_response.text)

