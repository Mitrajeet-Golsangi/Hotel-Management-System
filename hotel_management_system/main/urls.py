from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("reserve/", reserve, name="reserve"),
    path("book/<uuid:room_id>", book_room, name="book"),
    path("book_room/", confirm_booking, name="book_room"),
    path("my_rooms/", my_rooms, name="my_rooms"),
]
