#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

dm = DataManager()
dm.sheety_data_fetching()
sheet_data = dm.prices

fs = FlightSearch()
fd = FlightData()

notification_manager = NotificationManager()


lowestprice = []
for data in sheet_data:
    if data["iataCode"] == "":
       data["iataCode"] = fs.take_flight_name(data["city"])
       lowestprice.append(data['lowestPrice'])
       dm.updated_prices = sheet_data
       fd.flight_ticket(data["iataCode"])

    else:
        print("value present")



print(lowestprice)
dm.update_data()

for data in sheet_data:
    if fd.price < int(data['lowestPrice']):
        notification_manager.send_sms(
            message=f"Low price alert! Only £{fd.price} to fly from {fd.origin_city}-{fd.origin_airport} to {fd.destination_city}-{fd.destination_airport}."
        )