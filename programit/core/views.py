from datetime import timedelta
from django.shortcuts import render, redirect
from main.models.time_model import Time
from django.contrib.auth.forms import *
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

import logging

def home_view(request):
    if request.method == "POST":
        minutes = (request.POST.get("minutes"))
        seconds = (request.POST.get("seconds"))
        logging.info(f"{minutes}, {seconds}")
        minutes = [int(i) for i in minutes.split()]
        seconds = [int(i) for i in seconds.split()]
        minutes = " ".join(minutes)
        seconds = " ".join(seconds)
        
        end_time = timezone.now() + timedelta(minutes=minutes,seconds=seconds)
        Time.objects.create(user=request.user, end_time=end_time, start_time=timezone.now())
    timers = Time.objects.filter(user=request.user)
    return render(request, "home.html",{"timers": timers})


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
