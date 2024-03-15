from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('getweather/', get_weather_data, name='get_weather_data'),
]