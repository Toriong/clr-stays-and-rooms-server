from django.contrib import admin
from django.urls import path, include

from .views import GetStays, TestConnection




urlpatterns = [
    path('', TestConnection.as_view(), name='connectionCheck'),
    path('get-available-stays', GetStays.as_view(), name='get-available-stays'),
]