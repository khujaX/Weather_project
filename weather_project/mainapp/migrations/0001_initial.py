# Generated by Django 5.0.3 on 2024-03-15 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('temperature', models.FloatField()),
                ('pressure', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
