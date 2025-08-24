from django.db import models

class Time(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)
    stop_time = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True)

    def get_duration(self):
        if self.stop_time and self.start_time:
            return self.stop_time - self.start_time
        return f"in progress"

    def __str__(self):
        return f"{self.get_duration()}, {self.category}"