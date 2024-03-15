from django.db import models


class WeatherData(models.Model):
    city = models.CharField(max_length=30)
    temperature = models.FloatField()
    pressure = models.IntegerField()
    description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.city}'
