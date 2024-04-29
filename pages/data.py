import requests
from .models import Location
from decouple import config
import json

secret_key = config('SECRET_KEY')

def get_all_shelters():
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    params = {
        'location': '40.7128,-74.0060',
        'radius': 5000,
        'keyword': 'homeless shelter',
        'key': secret_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    next_page_token = data['next_page_token']
    # write to Location model
    for shelter in data['results']:
        location = Location(
            name=shelter['name'],
            vicinity=shelter['vicinity'],
            latitude=shelter['geometry']['location']['lat'],
            longitude=shelter['geometry']['location']['lng'],
            business_status=shelter['business_status']
        )
        location.save()
        get_individual_shelter(shelter['place_id'])
    
    i = 0
    while i < 4 and next_page_token != None:
        url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={next_page_token}&key={secret_key}'
        response = requests.get(url)
        data = response.json()
        next_page_token = data['next_page_token'] if 'next_page_token' in data else None

        for shelter in data['results']:
            location = Location(
                name=shelter['name'],
                vicinity=shelter['vicinity'],
                latitude=shelter['geometry']['location']['lat'],
                longitude=shelter['geometry']['location']['lng'],
                business_status=shelter['business_status']
            )
            location.save()
            get_individual_shelter(shelter['place_id'])
        i += 1


def get_individual_shelter(place_id):
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={secret_key}"
    response = requests.get(url)
    data = response.json()
    data = data['result']
    # write to Location model
    photo_ref = data["photos"][0]["photo_reference"] if "photos" in data else None
    photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=1000&photoreference={photo_ref}&key={secret_key}"
    if "opening_hours" in data and "weekday_text" in data["opening_hours"]:
        hours_array = data["opening_hours"]["weekday_text"]
    else:
        hours_array = [] 

    location = Location.objects.get(name=data['name'])
    location.hours_array = json.dumps(hours_array)
    location.photo_url = photo_url
    location.address = data['formatted_address']
    if "formatted_phone_number" in data:
        location.number = data['formatted_phone_number']
    else:
        location.number = "No phone number available"
    # if shelter name contains homeless services, remove from db
    if "homeless services" in location.name.lower():
        location.delete()
    else:
        location.save()