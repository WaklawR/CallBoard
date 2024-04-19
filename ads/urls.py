from django.urls import path

from .views import *

urlpatterns = [
    path("", AdvertList.as_view(), name="advert-list"),
]