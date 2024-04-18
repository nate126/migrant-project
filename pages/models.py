from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    vicinity = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    photo_url = models.URLField(max_length=255, null=True, blank=True)