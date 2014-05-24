#env/Scripts/python

import urllib.request



def main():
	API_KEY = "api_key=d0efe139-8e8d-4ff1-b020-7a71c9bbcb8e"

	
	data = urllib.request.urlopen("http://api.at.govt.nz/v1/gtfs/routes?" + API_KEY )
	print("Downloaded route data")
	
	
	print("Downloaded vehicle data")
	
	data_trips = urllib.request.urlopen("http://api.at.govt.nz/v1/gtfs/trips?" + API_KEY)
	print("downloaded trip data")

	data_stops = urllib.request.urlopen("http://api.at.govt.nz/v1/gtfs/stops?" + API_KEY)
	print("downloaded stop data")

	print("Acuired data, parsing ...")

	jsonData = data.readall().decode('utf-8')
	print("Decoded route data")

	jsonData_trips = data_trips.readall().decode('utf-8')
	print("Decoded trip data")

	jsonData_stops = data_stops.readall().decode('utf-8')
	print("Decoded stop data")
	

	routeFile = open("routeFile.txt", 'w')
	routeFile.write(jsonData)
	routeFile.close()

	print("Written route file")

	stopsFile = open("stopFile.txt", 'w')
	stopsFile.write(jsonData_stops)
	stopsFile.close()

	print("Written stops file")


	tripsFile = open("tripFile.txt", 'w')
	tripsFile.write(jsonData_trips)
	tripsFile.close()

	print("Written trips file")

	print("Finished")

if __name__ == "__main__":
	main()
