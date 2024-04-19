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
    import_locations_from_google_maps()
    locations = Location.objects.all()
    return render(request, 'pages/shelters.html', {"locations" : locations, "views": views})

def about_us(request):
    return render(request, 'pages/about-us.html', {"views": views})

def shelterTemplate(request):
    return render(request, 'pages/shelterTemplate.html', {"views": views})

def shelter_detail(request, shelter_id):
    shelter = get_object_or_404(Location, pk=shelter_id)
    return render(request, 'shelter_template.html', {'shelter': shelter, "views": views})
