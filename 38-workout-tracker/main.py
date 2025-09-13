from urllib.parse import uses_relative

import requests
from charset_normalizer.cli import query_yes_no

APP_ID = os.environ.get("NUTRITIONX_ID")
APP_API = os.environ.get("NUTRITIONX_API")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "Content-Type": 'application/json',
    "x-app-id": APP_ID,
    "x-app-key": APP_API
}

usr_input = input("Type your exercise: ")

params = {
    "query" = usr_input,
}
response = requests.post(url=exercise_endpoint, params=params, headers=headers)

print(response)

