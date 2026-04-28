from django.urls import path, include 
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/<str:pokemon>/', views.pokemon_details, name='pokemon_details'),
]
