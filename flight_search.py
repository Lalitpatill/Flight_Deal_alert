import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.city_name = ""
        self.TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/"
        self.API = "LbmN4OMtzSo310liQfnvj5txy2cJ3Njf"


    def take_flight_name(self, city_name):
        self.city_name = city_name
        header = {
            "apikey": self.API
        }
        search_param = {
            "term": self.city_name,
        }
        response = requests.get(url=f"{ self.TEQUILA_ENDPOINT}locations/query", params=search_param, headers=header)
        location_data = response.json()["locations"]
        # print(location_data)
        for data in location_data:
            if data["name"] == self.city_name:
                return data['code']
