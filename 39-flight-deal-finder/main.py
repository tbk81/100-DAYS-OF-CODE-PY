# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to
# achieve the program requirements.

# import os
# import requests
# from data_manager import DataManager

# AMADEUS_API_KEY = os.environ.get("AMADEUS_API_KEY")
# AMADEUS_API_SECRET = os.environ.get("AMADEUS_API_SECRET")
# AMADEUS_TOKEN = os.environ.get("AMADEUS_TOKEN")
#
# amadeus_endpnt = "https://test.api.amadeus.com"
# amadeus_token_endpnt = "/v1/security/oauth2/token"
# amadeus_city_endpnt = "/reference-data/locations/"
#
# amadeus_headers = {
#     "Authorization": f"Bearer {AMADEUS_TOKEN}"
# }

# Creating an access token
# amadeus_token_headers = {
#     "Content-Type": "application/x-www-form-urlencoded",
#     }
# data = {
#     "grant_type": "client_credentials",
#     "client_id": AMADEUS_API_KEY,
#     "client_secret": AMADEUS_API_SECRET
#     }
# token_response = requests.post(amadeus_endpnt + amadeus_token_endpnt, headers=amadeus_token_headers, data=data)
# print(token_response.text)

# city_params = {
#     "keyword": "PARIS"
# }

# print(amadeus_endpnt + amadeus_city_endpnt)
# city_response = requests.post(amadeus_endpnt + amadeus_city_endpnt, headers=amadeus_headers, params=city_params)
# print(city_response.text)
# print(city_response)

# data = DataManager()
# for price in data:
#     print
# print(data["prices"])


# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.
if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()