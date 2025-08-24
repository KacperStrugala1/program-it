from django.http import HttpResponse
from django.shortcuts import render
from main.models import Time

def home_view(request):
    times = Time.objects.all().values()
    context = {'times': times,}
    return render(request, "home.html", context)

def stats_view(request):
    return HttpResponse("There are profile stats")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def profile_view(request):
    return render(request, "profile.html")