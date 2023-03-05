from django.contrib import admin
from django.urls import path, include

from .views import GetStays, TestConnection
from rest_framework_simplejwt.views import (TokenRefreshView)




urlpatterns = [
    path('', TestConnection.as_view(), name='connectionCheck'),
    path('get-available-stays', GetStays.as_view(), name='get-available-stays'),
]