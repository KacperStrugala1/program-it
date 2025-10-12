from django.contrib import admin
from .models.time_model import Time
from .models.work_time import WorkTime

# Register your models here.
admin.site.register(Time)
admin.site.register(WorkTime)
