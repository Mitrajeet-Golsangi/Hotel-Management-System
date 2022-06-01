from django.db import models

from django.contrib.auth.models import User

# Create your models here.

SEX_CHOICE = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Rather not Say'),
]

QUALIFICATION_CHOICES = [
    (0, '12th pass'),
    (1, 'B.Tech.'),
    (2, 'BBA'),
    (3, 'MBA'),
]

CLEANLINESS_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]

STAFF_CHOICES = [
    ('M', "Management"),
    ('Service', (
            ('SH', 'House Keeping'),
            ('SK', 'Laundry'),
            ('SL', 'Kitchen'),
        )
    ),
]

class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='staff_user')
    
    staff_id = models.UUIDField()

    age = models.IntegerField()
    sex = models.CharField(max_length=100, choices=SEX_CHOICE)

    highest_qualification = models.CharField(max_length=100, choices=QUALIFICATION_CHOICES)

    staff_type = models.CharField(max_length=100, choices=STAFF_CHOICES)

    def __str__(self):
        return self.staff_id

class Guest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guest_user')

    id_proof = models.ImageField(upload_to='id_proof/%Y/%m/%d/')

    age = models.IntegerField()
    sex = models.CharField(max_length=100, choices=SEX_CHOICE)

    phone_number = models.BigIntegerField()

    def __str__(self):
        return self.email