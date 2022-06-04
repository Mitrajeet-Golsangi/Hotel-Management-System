from django.contrib import admin

from .models import *

# Register your models here.


def remove_registration(modeladmin, request, queryset):

    queryset.update(reserved=False)

    for d in queryset:
        Reserve.objects.filter(room=d.room_id).delete()

    remove_registration.short_description = "Remove Registration of Selected Rooms"


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
    actions = [
        remove_registration
    ]


@admin.register(Reserve)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'room',
        'start_date',
        'end_date',
        'additional_fees'
    )
