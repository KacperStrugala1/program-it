from django.contrib import admin
from .models import Time
from .models import WorkTime

# Register your models here.
admin.site.register(Time)
admin.site.register(WorkTime)
