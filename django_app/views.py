import re

from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django_app.models import Profile, Room, Message, Post, PostRating, PostComplain
from django.core.paginator import Paginator


def render_home(request: HttpRequest):
    sort = request.GET.get("sort", "desc")

    posts = Post.objects.all()

    match sort:
        case "date_asc":
            posts = posts.order_by("timestamp", "title")
        case "date_desc":
            posts = posts.order_by("-timestamp", "title")
        case _:
            posts = posts.order_by("title")

    selected_page = request.GET.get(key="page", default=1)
    pages = Paginator(object_list=posts, per_page=4)
    page = pages.page(number=selected_page)

    return render(
        request,
        "pages/Home.html",
        {"posts": page.object_list, "sort": sort, "page": page},
    )


def register_profile(request: HttpRequest):
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


def login_profile(request: HttpRequest):
    if request.method == "GET":
        return render(request, "pages/Login.html")

    elif request.method == "POST":
        username = str(request.POST["username"])
        password = str(request.POST["password"])

        user = authenticate(username=username, password=password)

        if user is None:
            error_message = "Username or password is incorrect"
            return render(request, "pages/Login.html", {"error": error_message})

        login(request, user)
        return redirect(reverse("home"))


def logout_profile(request: HttpRequest):
    logout(request)
    return redirect(reverse("login"))


def render_chats(request: HttpRequest):
    rooms = Room.objects.all()
    return render(request, "pages/ChatsList.html", {"rooms": rooms})


def render_room(request: HttpRequest, room_slug: str):
    rooms = Room.objects.all()
    room = Room.objects.get(slug=room_slug)
    messages = Message.objects.filter(room=room)[:30][::-1]
    return render(
        request,
        "components/chatComponent.html",
        {"messages": messages, "room": room, "rooms": rooms},
    )


def create_post(request: HttpRequest):
    if request.method == "POST":
        title = str(request.POST["title"])
        content = str(request.POST["content"])
        image = request.FILES.get("image", None)

        Post.objects.create(
            author=request.user, title=title, content=content, image=image
        )

        return redirect(reverse("home"))


def rate_post(request: HttpRequest, post_id: str, is_liked: str):
    author = request.user
    post = Post.objects.get(id=int(post_id))
    is_liked = True if is_liked == "1" else False

    try:
        liked_post = PostRating.objects.get(author=author, post=post)
        if liked_post.is_liked and is_liked:
            liked_post.delete()
        elif not liked_post.is_liked and not is_liked:
            liked_post.delete()
        else:
            liked_post.is_liked = is_liked
            liked_post.save()

    except Exception as _:
        PostRating.objects.create(author=author, post=post, is_liked=is_liked)

    return redirect(reverse("home"))


def edit_post(request: HttpRequest, post_id: str):
    if request.method == "GET":
        post = Post.objects.get(id=int(post_id))
        return render(request, "pages/EditPost.html", {"post": post})

    elif request.method == "POST":
        title = str(request.POST.get("title"))
        content = str(request.POST.get("content"))
        image = request.FILES.get("image", None)

        post = Post.objects.get(id=int(post_id))
        if post.title != title:
            post.title = title
        if post.content != content:
            post.content = content
        if image:
            post.image = image

        post.save()

        return redirect(reverse("home"))


def report_post(request: HttpRequest, post_id: str):
    post = Post.objects.get(id=int(post_id))
    author = request.user

    try:
        PostComplain.objects.get(author=author, post=post)
    except Exception as _:
        PostComplain.objects.create(author=author, post=post)

    return redirect(reverse("home"))


def render_complains(request: HttpRequest):
    complains = PostComplain.objects.all()
    return render(request, "pages/Complains.html", {"complains": complains})
