import datetime
import logging

from django.shortcuts import render, redirect
from main.models.time_model import Time
from main.models.profile_model import ProfileModel
from django.contrib.auth.forms import *
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


"""Views for the home page, login, registration, logout, and profile."""

def home_view(request):
    if not request.user.is_authenticated:
        return render(request, "home.html")
    
    if request.method == "POST":
        try:
            minutes = int(request.POST.get("minutes", 0))
            seconds = int(request.POST.get("seconds", 0))
        
            if minutes == 0 and seconds == 0:
                logging.warning("No time provided — timer was not created.")
                return redirect("")

            end_time = timezone.now() + datetime.timedelta(minutes=minutes, seconds=seconds)
            Time.objects.create(
                user=request.user,
                start_time=timezone.now(),
                end_time=end_time
            )
        except Exception as e:
            logging.error(f"Cannot create timers: {e}")
            return redirect("/")

    timers = Time.objects.filter(user=request.user).order_by("-start_time")
    return render(request, "home.html", {"timers": timers})

def login_view(request):
    if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.add_message(request, messages.ERROR, "Invalid credentials")
                return redirect('/log_into_acc')
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("/log_into_acc")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("log_into_acc/")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


@login_required(login_url="login")
def profile_view(request):
    
    if request.method == "POST":
        ProfileModel.objects.update(
            username=request.POST.get("username"),
            github_username=request.POST.get("github_username"),
            description=request.POST.get("description"),
            user=User.objects.get(username=request.user.username)
        )
        return redirect("/profile")
    profile_data = ProfileModel.objects.filter(user=request.user).first()
    return render(request, "profile.html", {"profile": profile_data})