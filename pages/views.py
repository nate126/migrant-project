from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_page_view(request):
    return HttpResponse('Hello, World!')

def shelter_page_view(request):
    return render(request, 'pages/shelters.html')