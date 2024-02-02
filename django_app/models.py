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
        auto_now_add=True,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-timestamp",)

    def __str__(self):
        return f"<Message {self.room.name} {self.content[:30]} ({self.id})/>"


class Post(models.Model):
    author = models.ForeignKey(
        verbose_name="Post author",
        db_index=True,
        primary_key=False,
        editable=False,
        blank=True,
        null=False,
        default=None,
        max_length=100,
        #
        to=User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        verbose_name="Post title",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )
    content = models.TextField(
        verbose_name="Post text",
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
        auto_now_add=True,
    )
    image = models.ImageField(
        verbose_name="Post image",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        upload_to="posts/images",
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-timestamp", "-content")

    def __str__(self):
        return f"<Post {self.title} {self.content[:30]} ({self.id})/>"


class PostRating(models.Model):
    author = models.ForeignKey(
        verbose_name="Author",
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
    post = models.ForeignKey(
        verbose_name="Post",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        #
        to=Post,
        on_delete=models.CASCADE,
    )
    is_liked = models.BooleanField(
        verbose_name="Liked or not",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=True,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-post", "-author")

    def __str__(self):
        return f"PostRating {self.post.title}({self.id}) | {self.is_liked}"
