from django.urls import path
from . import views

urlpatterns = [
    path('profile/<slug:slug>/', views.ProfileDetail.as_view(), name='profile-detail'),
]