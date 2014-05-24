from GTFS import gtfs_query

import json
# API_KEY = "api_key=d0efe139-8e8d-4ff1-b020-7a71c9bbcb8e"
# import urllib.request

class Stop:
    """
        This holds informaiton about a stop
    """

    def __init__(self, lat, long):
        stopData = gtfs_query('stops/geosearch?lat=' + str(lat) + '&lng=' + str(long) + '&distance=30')
        # stopData = urllib.request.urlopen('http://api.at.govt.nz/v1/gtfs/stops/geosearch?lat=' + str(lat) + '&lng=' + str(long) + '&distance=30' + '&' + API_KEY)
        # stopData = urllib.request.urlopen('http://api.at.govt.nz/v1/gtfs/stops/geosearch?lat=-36.843450&lng=174.766897&distance=30&api_key=d0efe139-8e8d-4ff1-b020-7a71c9bbcb8e')
        
        stopData = json.loads(stopData.read().decode('utf-8'))
        # print(stopData)
        
        stopData = stopData['response']
        stopData = stopData[0]

        self.stopInfo = stopData

        # The latitude and longitude position of the Stop
        self.stopPosition = (lat, long)