from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = (
        'room_id',
        'capacity',
        'room_type',
        'rate',
        'smoking',
        'floor',
        'reserved'
    )


@admin.register(Reserve)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'room',
        'start_date',
        'end_date',
        'additional_fees'
    )
