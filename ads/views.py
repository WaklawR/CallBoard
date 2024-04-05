from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from .models import Advert

class AdvertList(ListView):
    model = Advert
    template_name = "ads/advert_list.html"
    context_object_name = 'Advert'
    paginate_by = 100

class AdvertDetail(DetailView):
    """Подробно об объявлении"""
    model = Advert
    context_object_name = 'Advert'
    template_name = "ads/advert_detail.html"