import requests
from pprint import pprint
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = "https://api.sheety.co/ec65349e91485320e04bfe8fbbc6dae6/copyOfFlightDealsPart2/prices"
        self.username = "lalitpatill"
        self.password = "Lalitpatil@987"
        self.header = {
            "x-app-id": self.username,
            "x-app-key": self.password,
            "x-remote-user-id": "0"
        }
        self.prices = []
        self.updated_prices = []


    def sheety_data_fetching(self):
        response = requests.get(url=self.endpoint, headers=self.header)
        self.prices = response.json()["prices"]



    def update_data(self):
        for data in self.updated_prices:
            self.endpoint_put = f"https://api.sheety.co/ec65349e91485320e04bfe8fbbc6dae6/copyOfFlightDealsPart2/prices/{data['id']}"
            sheety_update_param ={
                "price": {
                    "iataCode": data["iataCode"]
                }
            }
            response = requests.put(url=self.endpoint_put, json=sheety_update_param )
            print(response.text)