#!../env/Scripts/python

import os
import json

def main():
	print("Beginning population script")

	stopFile = open('stopFile.txt')
	stopData = json.loads(stopFile.read())
	stops = stopData['response']
	stopFile.close()

	routeFile = open('routeFile.txt')
	routeData = json.loads(routeFile.read())
	routes = routeData['response']
	routeFile.close()

	tripFile = open('tripFile.txt')
	tripData = json.loads(tripFile.read())
	trips = tripData['response']
	tripFile.close()
	

	routeNumber = 0
	for route in routes:
		CreateRoute(route['route_short_name'], route['route_long_name'], route['route_id'])
		routeNumber += 1
	
	print(str(routeNumber) + ' routes')


	tripNumber = 0
	for trip in trips:
		CreateTrip(trip['trip_id'], trip['trip_headsign'], trip['service_id'], trip['trip_id'])
		tripNumber += 1

	print(str(tripNumber) + ' trips')


	stopNumber = 0
	for stop in stops:
		CreateStop(stop['stop_lat'], stop['stop_lon'], stop['stop_id'], stop['stop_name'])
		stopNumber += 1

	print(str(stopNumber) + ' stops')

def CreateStop(latitude, longitude, stop_id, stop_name):
	return Stop(latitude=latitude, longitude = longitude, stop_id = stop_id, stop_name = stop_name)

def CreateRoute(route_short_name, route_long_name, route_id):
	return Route(route_short_name = route_short_name, route_long_name = route_long_name, route_id = route_id)

def CreateTrip(route_id, trip_headsign, service_id, trip_id):
	return Trip(route_id = route_id, trip_headsign = trip_headsign, service_id = service_id, trip_id = trip_id)
	

if __name__ == "__main__":
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AlmostThere.settings')
	from Website.models import Stop, Route, Trip
	main()

	print("Finished population script")
