from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        verbose_name="User Profile",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        max_length=300,
        #
        to=User,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    avatar = models.ImageField(
        verbose_name="Avatar",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        upload_to="profile/avatars",
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-user",)

    def __str__(self):
        return f"<Profile {self.user.username} ({self.id})/>"


class Room(models.Model):
    name = models.CharField(
        verbose_name="Room name",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name="URL",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-name",)

    def __str__(self):
        return f"<Room {self.name} {self.slug} ({self.id})/>"


class Message(models.Model):
    user = models.ForeignKey(
        verbose_name="User",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        #
        to=User,
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        verbose_name="Room",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        #
        to=Room,
        on_delete=models.CASCADE,
    )
    content = models.TextField(
        verbose_name="Text message",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    timestamp = models.DateTimeField(
        verbose_name="Timestamp",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        max_length=300,
        auto_now_add=True,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-timestamp",)

    def __str__(self):
        return f"<Message {self.room.name} {self.content[:30]} ({self.id})/>"
