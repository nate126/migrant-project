from django.views.generic import ListView
from .models import *
from django.http import HttpResponse
from django.shortcuts import render



def home_page_view(request):
    return HttpResponse("Hello World")

def shelters(request):
    model= Locations
    context_object_name = "shelter"
    return render(request, 'pages/shelters.html',{context_object_name: model.objects.all()})




