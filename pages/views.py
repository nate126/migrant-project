from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd



# Create your views here.

def home_page_view(request):
    return HttpResponse('Hello, World!')

def shelters(request):
    # get first 150 from this dataset
    df = pd.read_csv("https://data.cityofnewyork.us/resource/bmxf-3rd4.csv")
    shelters = df.to_dict('records')
    return render(request, 'pages/shelters.html', {'shelters': shelters})
