from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CarParkModel
from .serializer import CarParkSerializer

def index(request):
    return render(request,"index.html")

@api_view(['GET'])
def all_car_parks_api(request):
    car_parks = CarParkModel.objects.all()
    serializer = CarParkSerializer(car_parks,many = True)
    return Response(serializer.data)