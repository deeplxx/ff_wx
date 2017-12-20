from django.urls import path
from apps.WaiMai.views import *

urlpatterns = [
    path('', Home, name='Home')
]
