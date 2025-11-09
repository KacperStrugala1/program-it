from django.db import models
from django.contrib.auth.models import User

class Time(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True)
    points = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.start_time and self.end_time:
            self.duration = self.end_time - self.start_time
        else:
            self.duration = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Query: {self.pk}, {self.category}"
    
    class Meta:
        verbose_name = "Focus duration"
