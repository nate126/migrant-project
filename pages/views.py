from django.views.generic import ListView
from .data import *
from django.http import HttpResponse
from django.shortcuts import render

# Add all views to view objects
views = [
        {"name": "Home", "url": "/"},
        {"name": "Shelters", "url": "/shelters/"},
        {"name": "About Us", "url": "/about-us/"},
        {"name": "ShelterTemplate", "url": "/shelter-Template"}
    ]

def near_me(request):
    return render(request, 'pages/nearme.html', {"views": views})

def home_page_view(request):
    return render(request, 'pages/home.html', {"views": views})
  
def shelters(request):
    import_locations_from_google_maps()
    locations = Location.objects.all()
    return render(request, 'pages/shelters.html', {"locations" : locations, "views": views})

def about_us(request):
    return render(request, 'pages/about-us.html', {"views": views})

def shelterTemplate(request):
    return render(request, 'pages/shelterTemplate.html', {"views": views})
