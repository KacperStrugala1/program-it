import datetime
import logging

from django.shortcuts import render, redirect
from main.models.time_model import Time
from main.models.profile_model import ProfileModel
from django.contrib.auth.forms import *
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View


class HomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "home.html")
        times = Time.objects.all().order_by("-start_time")
        return render(request, "home.html", {"times": times})

    def post(self, request):
        try:
            minutes = int(request.POST.get("minutes", 0))
            seconds = int(request.POST.get("seconds", 0))

            if minutes == 0 and seconds == 0:
                logging.warning("No time provided — timer was not created.")
                return redirect("")

            end_time = timezone.now() + datetime.timedelta(minutes=minutes, seconds=seconds)
            Time.objects.create(user=request.user, start_time=timezone.now(), end_time=end_time)
        except Exception as e:
            logging.error(f"Cannot create timers: {e}")
            return redirect("/")


class LoginView(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.add_message(request, messages.ERROR, "Invalid credentials")
            return redirect("/log_into_acc")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/log_into_acc")


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("log_into_acc/")


@login_required(login_url="login")
class ProfileView(View):

    def get(self, request):
        profile_data = ProfileModel.objects.filter(user=request.user).first()
        return render(request, "profile.html", {"profile": profile_data})

    def post(self, request):
        ProfileModel.objects.update(
            username=request.POST.get("username"),
            github_username=request.POST.get("github_username"),
            description=request.POST.get("description"),
            user=User.objects.get(username=request.user.username),
        )
        return redirect("/profile")
