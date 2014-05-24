from Math import Calculate_Distance_Between_Two_LatLong

class User(object):
    """
       Will hold information about the user.

       Please note that this iteration is using a straight line calculation - we are assuming that the distance between 
       two points on a map will be connected by a straight line. As we progress, we would need to journey plan and refine it
    """

    def __init__(self, lat, long, walkingSpeed = 4):
        # asigns lat and long values to the user, for later acess

        # The position in latitude and longitude
        self.position = (lat, long)

        # Speed is in meters per second.  So, here, 2km/h in meters per second
        # The reason for m/s is so that we can do minute calculations a little
        # easier
        self.walkingSpeed = float(walkingSpeed / 3.6)


    def calculate_distance_from_stop(self, stop):
        """
            Calculate the distance between you and the stop. We record the last distance, 
            for reference
        """

        # Uses the math library to calculate the distance in m
        distance_from_stop = Calculate_Distance_Between_Two_LatLong(self.position, stop.stopPosition)
        
        # makes it a part of the class
        self.distance = distance_from_stop

        # Returns the value, if not accessed through the object
        return distance_from_stop

    def calculate_walking_time(self, stop=None):
        """
            Calculates the time taken to the next stop

            Default to none, making it optional to use. If not specified, then uses the 
            last walking time
        """

        distance = None

        # Grabs the distance from the
        if stop != None:
            distance = self.calculate_distance_from_stop(stop)
        else:
            distance = self.distance

        walkingTime = distance / (2 / 3.6)

        # The time it would take to walk to the stop, in seconds
        self.walkingTime = walkingTime

        # Returns it, so it can be accessed that way as well
        return walkingTime


