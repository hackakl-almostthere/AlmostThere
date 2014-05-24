from django.db import models


class Stop(models.Model):

	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	
	stop_id = models.CharField(default=0, max_length=25)
	stop_name = models.CharField(default=0, max_length=50)


class Route(models.Model):
	route_short_name = models.CharField(default=0, max_length=50)
	route_long_name = models.CharField(default=0, max_length=100)

	route_id = models.CharField(default=0, max_length=20)

class Trip(models.Model):
	
	route_id = models.CharField(default=0, max_length=20)

	trip_headsign = models.CharField(default=0, max_length=20)

	service_id = models.CharField(default=0, max_length=25)

	trip_id = models.CharField(default=0, max_length=25)
