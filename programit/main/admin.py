from django.contrib import admin
from .models.time_model import Time, Category


# Register your models here.
admin.site.register(Time)
admin.site.register(Category)

