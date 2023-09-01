from flask import Flask, jsonify, request
from fetcher import fetch_data
from constants import CABIN_CLASS_MAP, TRIP_TYPE_MAP
import os

app = Flask(__name__)


def fetch_all_records_data(total_records, search_id, response_id):
	filter_req_data = {
		"searchID": search_id,
		"searchResponseID": response_id,
		"requestType": "deal",
		"searchType": "AirShopping",
		"fliterData": {
			"withBaggage": False,
			"pageination": {
				"page": 1,
				"limit": total_records
			}
		}
	}
	filter_url = os.getenv("FILTER_URL")
	resp_data = fetch_data(url=filter_url, request_data=filter_req_data)
	flights_info = resp_data["data"]["AirShoppingRS"]["Flights"]
	flights_data = []
	for flight_info in flights_info:
		data = flight_info["Data"]
		if data:
			interm_data = {
				"PricePerPerson": "USD {}".format(flight_info["RecomendedStopFare"])
			}
			interm_flights_info = []
			for curr_data in data:
				display_data = curr_data["DisplayData"]
				flight_data = {
					"DepartureAirportCode": display_data["DepartureAirportCode"],
					"DepartureDate": display_data["DepartureDate"],
					"DepartureTime": display_data["DepartureTime"],
					"ArrivalAirportCode": display_data["ArrivalAirportCode"],
					"ArrivalDate": display_data["ArrivalDate"],
					"ArrivalTime": display_data["ArrivalTime"],
					"JourneyTime": display_data["JourneyTime"],
					"Airlines": display_data["OperatingCarrierName"],
					"FlightNumber": display_data["MarketingInfo"],
					"Baggages": display_data["Baggages"],
					"SeatsLeft": display_data["FareSeatLeft"]
				}
				interm_flights_info.append(flight_data)
			interm_data["flightsInfo"] = interm_flights_info
			flights_data.append(interm_data)
	return flights_data


def parse_data(resp_data):
	status = resp_data["status"]
	status_code = resp_data["status_code"]
	if status == "success" or status_code == 200:
		search_id = resp_data["search_id"]
		search_response_id = resp_data["ShoppingResponseId"]
		data = resp_data["data"]
		filter_data = data["AirShoppingRS"]["FilterData"]
		pagination = filter_data["Pagination"]
		total_records = pagination["TotalRecords"]
		all_records_data = fetch_all_records_data(
			total_records, search_id, search_response_id)
		return all_records_data
	return None


def _parse_request(request_data, trip_type=None):
	flight_request_data = {
		"flight_req": {
			"trip_type": "oneway",
			"currency": "USD",
			"cabin": "Y",
			"sectors": [],
			"passengers": {
				"adult": 0,
				"child": 0,
				"lap_infant": 0,
				"infant": 0,
				"senior_citizen": 0,
				"youth": 0,
				"junior": 0
			},
			"shareUrlId": "",
			"search_type": "lowFareSearch"
		}
	}
	pax_details = request_data.get("paxDetails")
	flight_request_data["flight_req"]["passengers"]["adult"] = pax_details[
		"adultsCount"]
	flight_request_data["flight_req"]["passengers"]["child"] = pax_details[
		"childrenCount"]
	flight_request_data["flight_req"]["passengers"]["infant"] = pax_details[
		"infantsCount"]

	if not trip_type:
		trip_type = TRIP_TYPE_MAP[request_data["tripType"].lower()]
	flight_request_data["flight_req"]["trip_type"] = trip_type
	destinations = request_data.get("destination")
	if trip_type == "multi" and len(destinations) > 5:
		return 400, "Bad Request"
	elif trip_type == "return" and len(destinations) > 2:
		return 400, "Bad Request"
	elif trip_type == "oneway" and len(destinations) > 1:
		return 400, "Bad Request"

	for destination in destinations:
		sector = {
			"departure_date": destination["departureTime"],
			"destination": destination["arrivalLocationCode"],
			"origin": destination["departureLocationCode"],
			"sector_type": "departure"
		}
		flight_request_data["flight_req"]["sectors"].append(sector)

	cabin_class = request_data["cabinClass"]
	flight_request_data["flight_req"]["cabin"] = CABIN_CLASS_MAP[cabin_class]
	return flight_request_data


@app.route("/api/v1/fetch_flights", methods=["POST"])
@app.route("/api/v1/fetch_flights/<trip_type>", methods=["POST"])
def get_data(trip_type=None):
	try:
		request_data = request.get_json() # changed
		flight_request_data = _parse_request(request_data, trip_type)
		deal_url = os.getenv("DEAL_URL")
		headers = {
			"Portal-Origin": os.getenv("PORTAL_ORIGIN")
		}
		resp_data = fetch_data(
			url=deal_url, request_data=flight_request_data, headers=headers)
		flights_info = parse_data(resp_data)
		info = {
			"status": "Success",
			"data": flights_info
		}
	except Exception as e:
		info = {
			"status": "Failed",
			"error": str(e)
		}

	return jsonify(info)


if __name__ == '__main__':
	app.run()
