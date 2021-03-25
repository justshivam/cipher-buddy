from django.urls import path
from . import views

urlpatterns = [
    path('', views.peer),
    path('recText', views.recText),
    path('sendText', views.sendText),
    path('data', views.data)
]
