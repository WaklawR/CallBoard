from .models import Profile
from django.shortcuts import render
from django.views.generic import DetailView

def profile_detail(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/user-detail.html'