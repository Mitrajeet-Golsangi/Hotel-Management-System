from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    # --------------------------- Guest URLs --------------------------- #

    path("", index, name="home"),
    path("reserve/", reserve, name="reserve"),
    path("book/<uuid:room_id>", book_room, name="book"),
    path("book_room/", confirm_booking, name="book_room"),
    path("my_rooms/", my_rooms, name="my_rooms"),

    # --------------------------- Staff URLs --------------------------- #

    path("change_reservation/<uuid:id>",
         change_reservation_status, name="change_reservation"),
    path("update_reservation/", update_reservation, name="update_reservation"),
    path("delete_reservation/", delete_reservation, name="delete_reservation"),

]
