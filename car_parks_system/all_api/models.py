from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField

class CarParkModel(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.FloatField()
    now_capaticy = models.FloatField()
    latitude = models.FloatField()   #Enlem
    longitude = models.FloatField()  #Boylam
    
    def __str__(self,):
        return self.name
    
class CustomUser(AbstractUser):
    email = models.EmailField(unique = True)
    phone_number = PhoneField(blank=True,help_text="Telefon Numarasını Giriniz")
    
    def __str__(self):
        return self.username