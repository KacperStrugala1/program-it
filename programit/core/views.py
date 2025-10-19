from django.shortcuts import render, redirect
from main.models.time_model import Time
from main.models.work_time import WorkTime
from django.contrib.auth.forms import *
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

import logging

def home_view(request):
    times = Time.objects.order_by("-created_at")[:5]
    context = {
        "times": times,
    }

    try:
        action = request.POST.get("action")
        if request.method == "POST":
            if action == "start":
                Time.objects.create(start_time=timezone.now())
            elif action == "stop":
                if Time.objects.last():
                    if Time.end_time is None:
                        last_time_object = Time.objects.latest("id")
                        last_time_object.stop_time = timezone.now()
                        last_time_object.save()
            return redirect("home")
    except Exception as exc:
        logging.error(f"Error while POST method {exc}")
    return render(request, "home.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect("login")
    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required(login_url="login")
def profile_view(request):

    return render(request, "profile.html")
