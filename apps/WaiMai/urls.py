from django.urls import path
from apps.WaiMai import views

urlpatterns = [
    path('', views.Home, name='Home')
]
