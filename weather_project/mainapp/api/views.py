from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *


class WeatherView(viewsets.ModelViewSet):
    serializer_class = WeatherSerializer
    queryset = WeatherData.objects.all()
