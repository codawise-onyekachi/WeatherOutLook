from django.db import models

# Create your models here.





class WeatherAlert(models.Model):
    location = models.CharField(max_length=100)
    alert_type = models.CharField(max_length=100)
    threshold = models.FloatField()
    user_email = models.EmailField()
    # temperature = models.FloatField(null=False)
    # condition = models.CharField(max_length=255, null=True, blank=True)
    # humidity = models.FloatField(null=True, blank=True)
    # wind_speed = models.FloatField(null=True, blank=True)
    # air_pressure = models.FloatField(null=True, blank=True)
    # timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Alert for {self.location} ({self.alert_type})"



# from django.db import models

class WeatherData(models.Model):
    location = models.CharField(max_length=255)
    temperature = models.FloatField()
    condition = models.CharField(max_length=255)
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    air_pressure = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField(max_length=50)