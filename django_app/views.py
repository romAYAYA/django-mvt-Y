import re

from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse
from django_app.models import Profile


def render_home(request):
    return render(request, "pages/Home.html")


def register_profile(request):
    if request.method == "GET":
        return render(request, "pages/Register.html")

    elif request.method == "POST":
        username = str(request.POST["username"])
        password = str(request.POST["password"])
        confirm_password = str(request.POST["confirm-password"])
        user_avatar = request.FILES.get("user_avatar", None)

        if password != confirm_password and not re.match(
            r"^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{8,}$", password
        ):
            error_message = "Passwords do not match or should be stronger"
            return render(request, "pages/Register.html", {"error": error_message})

        user = User.objects.create(username=username, password=make_password(password))
        Profile.objects.create(user=user, avatar=user_avatar)

        login(request, user)
        return redirect(reverse("home"))


def login_profile(request):
    pass


def logout(request):
    pass
