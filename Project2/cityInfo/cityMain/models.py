from django.db import models

class CityName(models.Model):
  cityName = models.CharField(max_length=255)
  #lastname = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.cityName}"