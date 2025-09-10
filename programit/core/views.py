from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import Time
from django.contrib.auth.forms import *
from django.utils import timezone
import logging
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

def home_view(request):
    times = Time.objects.all()
    context = {'times': times,}
    
    try:
        action = request.POST.get("action")
        if request.method == "POST":
            if action == "start":
                Time.objects.create(start_time=timezone.now())
            elif action == "stop":
                last_time_object = Time.objects.latest('id')
                last_time_object.stop_time = timezone.now()
                last_time_object.save()
            return redirect("home")
    except Exception as exc:
        logging.error(f"Error while POST method {exc}")
    times = Time.objects.all()
    return render(request,"home.html", context)
    
def stats_view(request):
    times = Time.objects.all()
    context = {'times': times,}
    return render(request,"stats.html", context)

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
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

def profile_view(request):

    return render(request, "profile.html")