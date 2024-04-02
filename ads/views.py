from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .models import Advert

class AdvertList(ListView):
    model = Advert
    template_name = 'ads/advert_list.html'