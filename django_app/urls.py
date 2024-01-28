from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.render_home, name="home"),
    path("register/", views.register_profile, name="register"),
    path("login/", views.login_profile, name="login"),
    path("logout/", views.logout_profile, name="logout"),
]
