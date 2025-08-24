from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import Time
from django.contrib.auth.forms import *
from django.utils import timezone
import logging

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
    return HttpResponse("There are profile stats")

def login(request):
    #do login
    return render(request, "login.html")

def register(request):
    #continue register part 
    return render(request, "register.html")

def profile_view(request):
    return render(request, "profile.html")