from django.urls import path
from apps.WaiMai import views as wm_views

urlpatterns = [
    path('', wm_views.home, name='home')
]
