# Generated by Django 5.0.1 on 2024-01-31 10:59

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_app", "0008_alter_room_slug"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="timestamp",
            field=models.DateTimeField(
                auto_now_add=True, db_index=True, verbose_name="Timestamp"
            ),
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        default="",
                        max_length=300,
                        verbose_name="Post title",
                    ),
                ),
                (
                    "content",
                    models.TextField(blank=True, default="", verbose_name="Post text"),
                ),
                (
                    "timestamp",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Timestamp"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to="posts/images",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["jpg", "png", "jpeg"]
                            )
                        ],
                        verbose_name="Post image",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        default="",
                        max_length=300,
                        unique=True,
                        verbose_name="URL",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        default="",
                        max_length=100,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "ordering": ("-timestamp", "-content"),
            },
        ),
    ]
