from django.urls import path
import apps.WaiMai.views

urlpatterns = [
    path('', apps.WaiMai.views.Home, name='Home')
]
