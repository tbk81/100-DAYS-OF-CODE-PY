import os
import requests
from requests.auth import HTTPBasicAuth

sheety_endpoint = os.environ.get("SHEETY_FLIGHT_ENDPNT")
sheety_prices_endpoint = os.environ.get("SHEETY_PRICES_ENDPNT")

class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self._user = os.environ["SHEETY_FLIGHT_UN"]
        self._password = os.environ["SHEETY_FLIGHT_PW"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=sheety_endpoint, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        # pprint(data)
        return self.destination_data

    # In the DataManager Class, this makes a PUT request and uses the row id from sheet_data
    # to update the Google Sheet with the IATA codes.
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_prices_endpoint}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)
