from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")

def stats_view(request):
    return HttpResponse("There are profile stats")

def login(request):
    return render(request, "login.html")

def profile_view(request):
    return render(request, "profile.html")