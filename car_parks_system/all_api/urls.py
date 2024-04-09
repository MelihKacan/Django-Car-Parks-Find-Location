from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("all_car_parks_api",views.all_car_parks_api,name="all_car_parks_api"),
    path("user_login_api",views.user_login_api,name="user_login_api"),
    path("user_register_api",views.user_register_api,name="user_register_api"),
    path("user_logout_api",views.user_logout_api,name="user_logout_api"),
]
