from django.db import models
import uuid

from django.contrib.auth.models import User

# Create your models here.

ROOM_CHOICES = [
    ('Standard', 'Standard'),
    ('Standard No AC', 'Standard No AC'),
    ('Deluxe', 'Deluxe'),
    ('Suite', 'Suite'),
]


class Rooms(models.Model):
    room_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    capacity = models.IntegerField()
    room_type = models.CharField(max_length=100, choices=ROOM_CHOICES)
    rate = models.IntegerField()

    smoking = models.BooleanField(default=False)
    reserved = models.BooleanField(default=False)

    floor = models.IntegerField()


class Reserve(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user")
    room = models.ForeignKey(
        Rooms, on_delete=models.CASCADE, related_name="room")

    start_date = models.DateField()
    end_date = models.DateField()

    additional_fees = models.IntegerField()
