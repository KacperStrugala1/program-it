from datetime import timedelta
from django.db import models

class Time(models.Model):
    duration = models.DurationField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    def get_duration(self):
        try:
            duration = self.duration
        except (ValueError, AttributeError):
            duration = timedelta() 

    def __str__(self):
        return f"{self.get_duration()}, {self.category}"