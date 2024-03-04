from django.views.generic import ListView
from .data import *
from django.http import HttpResponse
from django.shortcuts import render

# Add all views to view objects
views = [
        {"name": "Home", "url": "/"},
        {"name": "Shelters", "url": "/shelters/"},
        {"name": "About Us", "url": "/about_us/"}
    ]

def near_me(request):
    return render(request, 'pages/nearme.html', {"views": views})

def home_page_view(request):
    return render(request, 'pages/home.html', {"views": views})

def shelters(request):
    data = getLocations()
    data = data["results"]
    return render(request, 'pages/shelters.html', {"shelters" : data, "views": views})

def about_us(request):
    return render(request, 'pages/about_us.html', {"views": views})
