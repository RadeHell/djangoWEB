from django.db import models

class city(models.Model):
  members = models.CharField(max_length=255)
  population = models.IntegerField()
  country = models.CharField(max_length=100)

  #lastname = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.members}"