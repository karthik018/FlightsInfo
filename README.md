# FlightsInfo
1. Clone the repo
2. cd into repo directory
# Create Virtual environment
````bash
python -m venv venv
source venv/bin/activate (linux)
venv\Scripts\Activate (windows)
````
# Install required dependencies from requirements.txt
````bash
pip install -r requirements.txt
````
3. Set these environment variables:
````bash
export FLASK_APP=main.py
export DEAL_URL=https://api.claritysso.com/api/flights/getResult/deal
export FILTER_URL=https://api.claritysso.com/api/flights/flightSearchFilterData
export PORTAL_ORIGIN=https://citiairtravel.com
````
4. Run Flask server either in pycharm or using command line
````bash
flask run
````

# Testing the API
1. I recommed to use [Postman](https://www.postman.com/downloads/) to test.
2. The service has two endpoints
````python
'/api/v1/flights_info'
'/api/v1/flights_info/trip_type' 
````
# /api/v1/flights_info
#### OneWay
````json
{
  "paxDetails": {
      "adultsCount": 0,
      "infantsCount": 0,
      "childrenCount": 0
  },
  "tripType": "oneway",
  "cabinClass": "Economy",
  "destination": [
      {
        "departureTime": "2023-09-01",
        "arrivalLocationCode": "DEL",
        "departureLocationCode": "HYD"
      }
  ]
}
````
#### RoundTrip
````json
{
  "paxDetails": {
      "adultsCount": 0,
      "infantsCount": 0,
      "childrenCount": 0
  },
  "tripType": "roundtrip",
  "cabinClass": "Economy",
  "destination": [
      {
        "departureTime": "2023-09-01",
        "arrivalLocationCode": "DEL",
        "departureLocationCode": "HYD"
      },
      {
        "departureTime": "2023-09-04",
        "arrivalLocationCode": "HYD",
        "departureLocationCode": "DEL"
      }
  ]
}
````
#### MultiCity
````json
{
  "paxDetails": {
      "adultsCount": 0,
      "infantsCount": 0,
      "childrenCount": 0
  },
  "tripType": "multicity",
  "cabinClass": "Economy",
  "destination": [
      {
        "departureTime": "2023-09-01",
        "arrivalLocationCode": "DEL",
        "departureLocationCode": "HYD"
      },
      {
        "departureTime": "2023-09-04",
        "arrivalLocationCode": "BOM",
        "departureLocationCode": "DEL"
      },
      {
        "departureTime": "2023-09-08",
        "arrivalLocationCode": "HYD",
        "departureLocationCode": "BOM"
      }
  ]
}
````
# /api/v1/flights_info/trip_type
````python
# trip_type is variable in this
# '/api/v1/flights_info/oneway'
# '/api/v1/flights_info/roundtrip'
# '/api/v1/flights_info/multicity'
````
#### OneWay
````json
{
  "paxDetails": {
      "adultsCount": 0,
      "infantsCount": 0,
      "childrenCount": 0
  },
  "cabinClass": "Economy",
  "destination": [
      {
        "departureTime": "2023-09-01",
        "arrivalLocationCode": "DEL",
        "departureLocationCode": "HYD"
      }
  ]
}
````
#### RoundTrip
````json
{
  "paxDetails": {
      "adultsCount": 0,
      "infantsCount": 0,
      "childrenCount": 0
  },
  "cabinClass": "Economy",
  "destination": [
      {
        "departureTime": "2023-09-01",
        "arrivalLocationCode": "DEL",
        "departureLocationCode": "HYD"
      },
      {
        "departureTime": "2023-09-04",
        "arrivalLocationCode": "HYD",
        "departureLocationCode": "DEL"
      }
  ]
}
````
#### MultiCity
````json
{
  "paxDetails": {
      "adultsCount": 0,
      "infantsCount": 0,
      "childrenCount": 0
  },
  "cabinClass": "Economy",
  "destination": [
      {
        "departureTime": "2023-09-01",
        "arrivalLocationCode": "DEL",
        "departureLocationCode": "HYD"
      },
      {
        "departureTime": "2023-09-04",
        "arrivalLocationCode": "BOM",
        "departureLocationCode": "DEL"
      },
      {
        "departureTime": "2023-09-08",
        "arrivalLocationCode": "HYD",
        "departureLocationCode": "BOM"
      }
  ]
}
````
