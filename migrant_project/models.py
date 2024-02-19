from django.db import models

import pandas as pd
from django.contrib.auth.models import User
from migrant_project.models import Products

csv_file_path = "https://data.cityofnewyork.us/resource/bmxf-3rd4.csv"
df = pd.read_csv(csv_file_path)

# Create your models here.


class ShelterInfo(models.Model):
    center_name = models.CharField(max_length=255,default='admin')
    borough = models.CharField(max_length=255,default='admin')
    address = models.CharField(max_length=255,default='admin')
    #do I need integer for address and comments code?
    comments = models.CharField(max_length=255,default='admin')
    postcode = models.DecimalField(max_digits=6)
    latitude = models.DecimalField(max_digits=2,decimal_places=6)
    longitude = models.DecimalField(max_digits=2,decimal_places=6)


for index, row in df.iterrows():
    product = Products(
        center_name = row['center_name'],
        borough = row['borough'],
        address = row['address'],
        comments = row['comments'],
        postcode = row['postcode'],
        latitude = row['latitude'],
        longitude = row['longitude'],
    )
    product.save()

