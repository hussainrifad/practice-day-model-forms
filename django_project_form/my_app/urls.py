from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('form/', views.form, name = 'formpage'),
    path('addartist/', views.artist, name='addartist'),
]