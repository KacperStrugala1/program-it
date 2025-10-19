from datetime import timedelta
from django.db import models
from datetime import datetime, date, timedelta, time


class Time(models.Model):
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=datetime.now)

    

    def get_duration(self):
        
        if not self.start_time or not self.end_time:
            return None
        
        start = self.start_time
        end = self.end_time
        if isinstance(start, str):
            start = time.fromisoformat(start)
        if isinstance(end, str):
            end = time.fromisoformat(end)

        start_dt = datetime.combine(date.today(), start)
        end_dt = datetime.combine(date.today(), end)

        if end_dt < start_dt:
            end_dt += timedelta(days=1)
        duration = end_dt - start_dt
        
        return str(duration)

    def __str__(self):
        return f"{self.get_duration()}, {self.category}"
    
    class Meta:
        verbose_name = "Focus duration"
