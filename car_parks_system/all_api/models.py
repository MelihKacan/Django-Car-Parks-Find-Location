from typing import Any
from django.db import models

class CarParkModel(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.FloatField()
    now_capaticy = models.FloatField()
    latitude = models.FloatField()   #Enlem
    longitude = models.FloatField()  #Boylam
    
    def __str__(self,):
        return self.name