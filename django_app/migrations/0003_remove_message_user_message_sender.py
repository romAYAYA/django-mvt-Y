# Generated by Django 5.0.1 on 2024-01-28 17:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_app", "0002_message"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="user",
        ),
        migrations.AddField(
            model_name="message",
            name="sender",
            field=models.ForeignKey(
                blank=True,
                default="",
                max_length=100,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Sender",
            ),
        ),
    ]
