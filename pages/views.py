from .data import *
from django.shortcuts import get_object_or_404, render
from .models import Location

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
    location = get_object_or_404(Location, slug=location_slug)
    hours = location.hours_array
    hours = json.loads(hours)
    return render(request, 'pages/shelter_detail.html', {'shelter': location, "views": views, 'hours': hours})
