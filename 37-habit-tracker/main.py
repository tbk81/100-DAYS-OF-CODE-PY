import os
import requests
from datetime import datetime

# https://pixe.la/@falseoctet
# https://pixe.la/v1/users/falseoctet/graphs/graph1.html

# Creates the Pixela account
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "falseoctet"
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph1"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": TOKEN
    }

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# new_graph_params = {
#     "id": GRAPH_ID,
#     "name": "Net+ study time",
#     "unit": "minutes",
#     "type": "int",
#     "color": "momiji",
# }
#
# response = requests.post(url=graph_endpoint, json=new_graph_params, headers=headers)
# print(response.text)

# today = datetime.now()
today = datetime(year=2025, month=9, day=9)  # yesterday's date to backfill
day = today.strftime("%Y%m%d")
pixel_change_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day}"
# print(today)

put_pixel_params = {
    "quantity": "300",
    }
# print(pixel_params["date"])
# response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)

# response = requests.put(url=pixel_change_endpoint, json=put_pixel_params, headers=headers)
# print(response.text)

response = requests.delete(url=pixel_change_endpoint, headers=headers)
print(response.text)



