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
    path("create_post/", views.create_post, name="create_post"),
    path("post/<str:post_id>/rating/<str:is_liked>", views.rate_post, name="rate_post"),
    path("post/edit/<str:post_id>", views.edit_post, name="edit_post"),
    path("post/complain/<str:post_id>", views.report_post, name="report_post"),
    path("complains/", views.render_complains, name="complains")
]

websocket_urlpatterns = [path("ws/chat/<slug:room_name>/", ChatConsumer.as_asgi())]
