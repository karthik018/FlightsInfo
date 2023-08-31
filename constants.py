FLIGHT_REQUEST_DATA = {
	"flight_req": {
		"trip_type":"oneway",
		"currency":"USD",
		"cabin":"Y",
		"sectors":[],
		"passengers": {
			"adult":1,
			"child":1,
			"lap_infant":0,
			"infant":1,
			"senior_citizen":0,
			"youth":0,
			"junior":0
		},
		"shareUrlId":"",
		"search_type":"lowFareSearch"
	}
}

CABIN_CLASS_MAP = {
	"Economy": "Y",
	"PremiumEconomy": "S",
	"Business": "C",
	"FirstClass": "F"
}

TRIP_TYPE_MAP = {
	"oneway": "oneway",
	"roundtrip": "return",
	"multicity": "multi"
}