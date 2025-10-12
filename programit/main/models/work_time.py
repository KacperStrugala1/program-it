from datetime import timedelta
from django.db import models

class WorkTime(models.Model):
    duration = models.DurationField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Task "
    
  