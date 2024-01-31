from django.urls import path
from django_app import views
from django_app.consumers import ChatConsumer

urlpatterns = [
    path("", views.render_home, name="home"),
    path("register/", views.register_profile, name="register"),
    path("login/", views.login_profile, name="login"),
    path("logout/", views.logout_profile, name="logout"),
    path("chat/", views.render_chats, name="chat"),
    path("chat/<slug:room_slug>/", views.render_room, name="room"),
    path("create_post/", views.create_post, name="create_post")
]

websocket_urlpatterns = [path("ws/chat/<slug:room_name>/", ChatConsumer.as_asgi())]
