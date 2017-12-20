from django.urls import path
from apps.WaiMai.views import Home

urlpatterns = [
    path('', Home, name='Home')
]
