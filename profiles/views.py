from .models import Profile
from django.shortcuts import render
from django.views.generic import DetailView

class Profile_Detail(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/user-detail.html'