import requests

def getLocations(nextPageToken = "", counter = 0, data = []):
    pageToken = ""
    if nextPageToken != "":
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken=' + nextPageToken + '&key=AIzaSyBudDAel4hrhurK0iGmhl9H3kMvzwZ3IqY'
    else:
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.7128,-74.0060&radius=5000&keyword=homeless%20shelter&key=AIzaSyBudDAel4hrhurK0iGmhl9H3kMvzwZ3IqY'
    response = requests.request("GET", url)
    response = response.json()
    data.extend(response["results"])
    if counter > 3:
        return data
    pageToken = response.get("next_page_token", "")
    counter+=1
    return getLocations(pageToken, counter, data)