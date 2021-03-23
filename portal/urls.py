from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('contact', views.contact),
    path('about', views.about),
    path('complaint', views.complaint),
    path('status', views.status)
]
