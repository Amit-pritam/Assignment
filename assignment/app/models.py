from django.db import models

class Country_Model(models.Model):
	Country_name = models.CharField(max_length = 100)

class State_Model(models.Model):
	state_name = models.CharField(max_length = 100)

class City_Model(models.Model):
	city_name = models.CharField(max_length = 100)


class Location_Model(models.Model):
	location_name = models.CharField(max_length = 100)

class UserData_Model(models.Model):
	Country_name = models.ManyToManyField(Country_Model)
	state_name = models.ManyToManyField(State_Model)
	city_name = models.ManyToManyField(City_Model)
	location_name = models.ManyToManyField(Location_Model)









