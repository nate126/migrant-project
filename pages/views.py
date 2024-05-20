from .data import *
from django.shortcuts import get_object_or_404, render
from .models import Location
from .donations import matchShelters
from .models import Location



def shelter_detail(request, location_slug):
    shelter_location = get_object_or_404(Location, slug=location_slug)
    return render(request, 'pages/shelter_detail.html', {'shelter_location': shelter_location})



# Add all views to view objects
views = [
        {"name": "Home", "url": "/"},
        {"name": "Shelters", "url": "/shelters/"},
        {"name": "About Us", "url": "/about-us/"},
    ]

def near_me(request):
    return render(request, 'pages/nearme.html', {"views": views})

def home_page_view(request):
    return render(request, 'pages/home.html', {"views": views})
  
def shelters(request):
    locations = Location.objects.all()
    return render(request, 'pages/shelters.html', {"locations" : locations, "views": views})

def about_us(request):
    return render(request, 'pages/about-us.html', {"views": views})






def shelter_detail(request, location_slug):
    shelter_location = get_object_or_404(Location, slug=location_slug)
    donate_link = matchShelters(shelter_location.name)  # Get the donate link using the shelter name
    hours = json.loads(shelter_location.hours_array)
    return render(request, 'pages/shelter_detail.html', {
        'shelter_location': shelter_location,
        'hours': hours,
        'donate_link': donate_link
    })
