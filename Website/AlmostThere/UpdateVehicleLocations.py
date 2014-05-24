
import urllib.request
import json

import time

API_KEY = 'api_key=d0efe139-8e8d-4ff1-b020-7a71c9bbcb8e'

def UpdateVehicle():


    while(True):
        vehicles = UpdateData()
        UpdateModels(vehicles)
        print("Completed")
        time.sleep(5)
 

def UpdateData():
    data = urllib.request.urlopen('http://api.at.govt.nz/v1/public/realtime/vehiclelocations?' + API_KEY)
    vehicles = json.loads(data.read().decode('utf-8'))
    vehicles = vehicles['response']['entity']

    return vehicles

def UpdateModels(vehicles):
    

    for vehicle in vehicles:

        try:
            vehicleData = Vehicle.objects.get(vehicle_id=vehicle['vehicle']['vehicle']['id'])
        except Vehicle.DoesNotExist:
            vehicleData = None


        if  vehicleData != None:
            vehicleData = Vehicle.objects.get(vehicle_id=vehicle['vehicle']['vehicle']['id'])
            
            vehicleData.trip_id = vehicle['vehicle']['trip']['trip_id']

            vehicleData.latitude = vehicle['vehicle']['position']['latitude']
            vehicleData.longitude = vehicle['vehicle']['position']['longitude']

            vehicleData.timestamp = vehicle['vehicle']['timestamp']

            vehicleData.save()

        elif vehicleData == None:
            vehicleCreate = Vehicle(route_id = vehicle['vehicle']['trip']['route_id'],
                              trip_id = vehicle['vehicle']['trip']['trip_id'],
                              latitude = vehicle['vehicle']['position']['latitude'],
                              longitude = vehicle['vehicle']['position']['longitude'],
                              timestamp = vehicle['vehicle']['timestamp'],
                              data_id = vehicle['id'],
                              vehicle_id = vehicle['vehicle']['vehicle']['id'])

            vehicleCreate.save()

if __name__ == '__main__':
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AlmostThere.settings")
    from Website.models import Vehicle

    UpdateVehicle()