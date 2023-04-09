from django.contrib import admin
from django.urls import path
from .views import Rooms


urlpatterns = [
    path('post', Rooms.as_view(), name='post-new-rooms'),
    path('edit', Rooms.as_view(), name='edit-new-rooms')
]

