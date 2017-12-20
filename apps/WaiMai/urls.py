from django.urls import path
from apps.WaiMai import views

urlpatterns = [
    path('index/', views.index, name='index')
]