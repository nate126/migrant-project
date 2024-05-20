from django.db import models
from django.utils.text import slugify

class Location(models.Model):
    name = models.CharField(max_length=255)
    vicinity = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    photo_url = models.URLField(max_length=255, null=True, blank=True)
    hours_array = models.JSONField(null=True, blank=True)
    business_status = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class MatchShelters(models.Model):
    shelter_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    donate_link = models.URLField(max_length=200)  # Assuming it is a URL
    def __str__(self):
        return self.shelter_location.name
