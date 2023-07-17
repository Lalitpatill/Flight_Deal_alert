import requests
import datetime as dt


now = dt.datetime.now().date().strftime("%d/%m/%Y")
date_to = dt.datetime.now() + dt.timedelta(days=60)
updated_date_to = date_to.date().strftime("%d/%m/%Y")


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.origin_city = "London"
        self.origin_airport = "LCY"
        self.destination_city = ""
        self.destination_airport=""
        self.price = 0
        self.ENDPOINT_FLIGHTSEARCH = "https://api.tequila.kiwi.com/v2/search"

    def flight_ticket(self, desti_code):
        header = {
            "apikey": "LbmN4OMtzSo310liQfnvj5txy2cJ3Njf"
        }

        flight_param = {
            "fly_from": self.origin_airport,
            "fly_to": desti_code,
            "curr": "GBP",
            "price_from": 50,
            "prcie_to": 380,
            "date_from": now,
            "date_to": updated_date_to


        }
        response = requests.get(url=self.ENDPOINT_FLIGHTSEARCH, params=flight_param, headers=header)
        # print(response.json())
        for data in response.json()['data']:
            self.destination_city = data["cityTo"]
            self.destination_airport = data["cityCodeTo"]





