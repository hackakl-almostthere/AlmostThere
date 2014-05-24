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
	

	routeList = []
	for route in routes:
		routeItem = CreateRoute(route['route_short_name'], route['route_long_name'], route['route_id'])
		routeList.append(routeItem)
	
	Route.objects.bulk_create(routeList)

	print(str(len(routeList)) + ' routes')
	

	tripList = []
	for trip in trips:
		tripItem = CreateTrip(trip['trip_id'], trip['trip_headsign'], trip['service_id'], trip['trip_id'], trip['direction_id'])
		tripList.append(tripItem)

	Trip.objects.bulk_create(tripList)

	print(str(len(tripList)) + ' trips')


	stopList = []
	for stop in stops:
		stopItem = CreateStop(stop['stop_lat'], stop['stop_lon'], stop['stop_id'], stop['stop_name'])
		stopList.append(stopItem)

	Stop.objects.bulk_create(stopList)

	print(str(len(stopList)) + ' stops')

def CreateStop(latitude, longitude, stop_id, stop_name):
	return Stop(latitude=latitude, longitude = longitude, stop_id = stop_id, stop_name = stop_name)

def CreateRoute(route_short_name, route_long_name, route_id):
	return Route(route_short_name = route_short_name, route_long_name = route_long_name, route_id = route_id)

def CreateTrip(route_id, trip_headsign, service_id, trip_id, direction_id):
	return Trip(route_id = route_id, trip_headsign = trip_headsign, service_id = service_id, trip_id = trip_id, direction_id = direction_id)
	

if __name__ == "__main__":
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AlmostThere.settings')
	from Website.models import Stop, Route, Trip
	main()

	print("Finished population script")
