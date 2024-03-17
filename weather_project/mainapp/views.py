from django.shortcuts import render, redirect
from .models import WeatherData
import requests
import json


def main(request):

    return render(request, 'mainapp/index.html')


def get_weather_data(request):
    api_key = "0a546f6b8b828311afba1f6fa5566665"
    city = "Nottingham"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={},gb&APPID={}'

    weather_db = WeatherData.objects.all()
    for data in weather_db:
        WeatherData.objects.filter(id=data.id).delete()

    weather_info = requests.get(url.format(city, api_key)).json()
    WeatherData.objects.create(city=weather_info['name'], temperature=weather_info['main']['temp'], pressure=weather_info['main']['pressure'], description=weather_info['weather'][0]['description'])

    return redirect("main")
