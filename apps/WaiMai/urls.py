from django.urls import path
from . import views as waimai_views

urlpatterns = [
    path('', waimai_views.Home, name='Home')
]
