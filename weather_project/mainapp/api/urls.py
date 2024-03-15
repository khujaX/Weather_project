from django.urls import path
from .views import *

urlpatterns = [
    path('weather/view/', WeatherView.as_view({'get': 'list'}), name="api-weather-view")
]