from django.urls import path
from apps.WaiMai import views

urlpatterns = [
    path('', views.index, name='index')
]