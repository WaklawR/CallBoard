from django.urls import path

from . import views


urlpatterns = [
    path('<int:pk>/', views.Profile_Detail.as_view()),

]