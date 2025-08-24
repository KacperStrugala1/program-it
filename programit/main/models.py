from django.db import models


class Time(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)
    stop_time = models.DateTimeField(null=True, blank=True)
    duration = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.stop_time - self.start_time}" or "in progress"