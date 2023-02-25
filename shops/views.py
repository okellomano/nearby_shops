from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

from .models import Shop


latitude = -1.2982549
longitude = 36.7630381

user_location = Point(longitude, latitude, srid=4326)


class ShopListView(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[0:5]
    template_name = 'index.html'

