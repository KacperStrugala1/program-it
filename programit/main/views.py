from django.shortcuts import render,redirect
from .models import Time
from django.utils import timezone

# Create your views here.
def start_time(request):
    Time.objects.create(start_time=timezone.now())
    return redirect("/",)

def stop_time(request):
    pass

