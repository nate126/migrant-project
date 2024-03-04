from django.views.generic import ListView
from .data import *
from django.http import HttpResponse
from django.shortcuts import render



def home_page_view(request):
    return HttpResponse("Hello World")

def shelters(request):
    data = getLocations()
    data = data["results"]
    return render(request, 'pages/shelters.html', {"shelters" : data})

def about_us(request):
    return render(request, 'pages/about_us.html')