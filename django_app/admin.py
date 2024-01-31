from django.contrib import admin
from django_app.models import Profile, Message, Room, Post

admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Room)
admin.site.register(Post)