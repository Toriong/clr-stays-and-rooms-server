from django.contrib import admin
from django.urls import path, include

from .views import GetAvailableRooms, TestConnection, GetUserReservations




urlpatterns = [
    path('', TestConnection.as_view(), name='connectionCheck'),
    path('get-available-rooms', GetAvailableRooms.as_view(), name='get-available-rooms'),
    path('get-user-reservations', GetUserReservations.as_view(), name='get-user-reservations')
]