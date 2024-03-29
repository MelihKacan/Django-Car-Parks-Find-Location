from rest_framework import serializers
from .models import CarParkModel


class CarParkSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length=100)
    capacity = serializers.FloatField()
    now_capaticy = serializers.FloatField()
    latitude = serializers.FloatField()   #Enlem
    longitude = serializers.FloatField()  #Boylam