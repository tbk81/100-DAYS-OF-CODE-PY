import requests
import os
from pprint import pprint
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
        self.sheety_endpoint = os.environ.get("SHEETY_FLIGHT_ENDPNT")
        auth_header = {
            "Authorization": f"Bearer {self.SHEETY_TOKEN}"
        }
        data = requests.get(url=self.sheety_endpoint, headers=auth_header)
        print(data.text)
