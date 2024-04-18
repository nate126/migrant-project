import requests
import logging
from .models import Location

logger = logging.getLogger(__name__)

def query_google_maps_locations():
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    params = {
        'location': '40.7128,-74.0060',
        'radius': 5000,
        'keyword': 'shelter',
        'key': 'AIzaSyBmn-SLAxuhmUFHzLd3pwwFKfQx51iBwZg'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def import_locations_from_google_maps():
    try:
        data = query_google_maps_locations()
        locations = []
        for result in data.get("results", []):
            location_name = result.get("name", "Unknown")
            location_vicinity = result.get("vicinity", "Unknown")
            location_lat = result["geometry"]["location"]["lat"]
            location_lon = result["geometry"]["location"]["lng"]
            location_address = result.get("vicinity", "Unknown")
            location_number = result.get("formatted_phone_number", "")
            if not location_number:
                location_number = "Unknown"
            location_photo_reference = result.get("photos", [{}])[0].get("photo_reference", "")
            photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={location_photo_reference}&key=AIzaSyBmn-SLAxuhmUFHzLd3pwwFKfQx51iBwZg"
            locations.append(Location(
                name=location_name,
                vicinity=location_vicinity,
                latitude=location_lat,
                longitude=location_lon,
                address=location_address,
                number=location_number,
                photo_url=photo_url
            ))
        Location.objects.bulk_create(locations)
    except Exception as e:
        logger.error(f"Error importing locations from Google Maps API: {e}")
