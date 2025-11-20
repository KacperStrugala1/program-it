from django.contrib import admin
from .models.time_model import Time
from .models.profile_model import ProfileModel
from .models.backlog_model import Backlog


# Register your models here.
admin.site.register(Time)
admin.site.register(ProfileModel)
admin.site.register(Backlog)
