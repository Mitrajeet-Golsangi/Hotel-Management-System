# Generated by Django 4.0.4 on 2022-06-02 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_rooms_reserved_alter_rooms_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='user',
            field=models.ForeignKey(default=25, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
