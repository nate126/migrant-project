from django.db import models
import requests
import os

def getLocations():
    GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": "40.7128,-74.0060", 
        "radius": 5000,  
        "keyword": "homeless shelter", 
        "key": GOOGLE_MAPS_API_KEY,
    }
    response = requests.get(base_url, params=params)
    results = response.json().get('results', [])

    for result in results:
        name = result.get('name')
        address = result.get('vicinity')
        city, country_zip = address.split(', ')[-2:]
        country, zip_code = country_zip.split(' ')
        Locations.objects.create(
            name=name,
            address=address,
            city=city,
            country=country,
            zip_code=zip_code,
        )

class Locations(models.Model):
    club = models.CharField(max_length=500, blank= True, null= True)
    name = models.CharField(max_length=500)
    zipcode = models.CharField(max_length=200, blank= True, null= True)
    city = models.CharField(max_length=200, blank= True, null= True)
    country = models.CharField(max_length=200, blank= True, null= True)
    adress = models.CharField(max_length=200, blank= True, null= True)
    created_at = models.DateTimeField(auto_now_add=True, blank= True, null= True)
    # edited_at = created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name