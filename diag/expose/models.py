from django.db import models

# Create your models here.
class vehicle_data(models.Model):
    '''
    Class definition for vehicle data read from OBD-II chip
    '''
    #add fields here
    rpm = models.FloatField()
    
class location_data(models.Model):
    '''
    Class definition of location data generated by GPS module in smartphone