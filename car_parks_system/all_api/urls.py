from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("all_car_parks_api",views.all_car_parks_api,name="all_car_parks_api")
]
