import datetime
import logging

from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models.time_model import Time
from main.models.profile_model import ProfileModel
from main.models.backlog_model import Backlog   
from django.contrib.auth.forms import *
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from django.utils.decorators import method_decorator


class HomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "home.html", {"form": TaskForm()})
        times = Time.objects.all().order_by("-start_time")
        return render(request, "home.html", {"times": times, "form": TaskForm()})

    def post(self, request):
        
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Backlog.objects.create(
                name = form.cleaned_data['task_name'],
                category = form.cleaned_data['task_category'],
                description = form.cleaned_data['task_description']
            )
            
        else:
            form = TaskForm()
            return HttpResponse("Invalid data inserted in form")
        return redirect("HomeView")

class LoginView(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("HomeView")
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
            return redirect("/log_into_acc/")


@method_decorator(login_required, name='dispatch')
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
