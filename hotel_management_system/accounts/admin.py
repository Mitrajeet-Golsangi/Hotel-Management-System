from django.contrib import admin
from django.db.models import F
from .models import *


# Register your models here.

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):

    list_display = (
        'staff_id',
        'age',

        'sex',

        'highest_qualification',

        'staff_type'

    )


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'id_proof',
        'age',

        'sex',

        'phone_number'

    )
