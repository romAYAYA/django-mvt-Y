# Generated by Django 5.0.1 on 2024-01-31 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_app", "0009_alter_message_timestamp_post"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="user",
        ),
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                blank=True,
                default=None,
                editable=False,
                max_length=100,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to="django_app.profile",
                verbose_name="Post author",
            ),
        ),
    ]
