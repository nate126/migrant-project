import requests
from os import getenv


def getLocations():
    GOOGLE_MAPS_API_KEY = getenv('GOOGLE_MAPS_API_KEY')
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.7128,-74.0060&radius=5000&keyword=homeless%20shelter&key=AIzaSyBudDAel4hrhurK0iGmhl9H3kMvzwZ3IqY'
    response = requests.request(url=url, method="GET")
    data = response.json()
    return data