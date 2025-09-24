import os
import requests

class FlightSearch:

    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API_KEY")
        self._api_secret = os.environ.get("AMADEUS_API_SECRET")
        self._token = self._get_new_token()
        self.amadeus_endpnt = "https://test.api.amadeus.com"
        self.amadeus_token_endpnt = "/v1/security/oauth2/token"

    def _get_new_token(self):
        """
        Generates the authentication token used for accessing the Amadeus API and returns it.
        This function makes a POST request to the Amadeus token endpoint with the required
        credentials (API key and API secret) to obtain a new client credentials token.
        Upon receiving a response, the function updates the FlightSearch instance's token.
        Returns:
            str: The new access token obtained from the API response.
        """
        amadeus_token_headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            }
        data = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
            }
        token_response = requests.post(self.amadeus_endpnt + self.amadeus_token_endpnt, headers=amadeus_token_headers, data=data)
        print(f"Your token is {token_response.json()['access_token']}")
        print(f"Your token expires in {token_response.json()['expires_in']} seconds")
        return token_response.json()['access token']

    def get_destination_code(self, city_name):
        # code = "TESTING"
        # return code
        pass
