from django.shortcuts import render, redirect
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def home_view(request):
    
    return render(request, "home.html")


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
