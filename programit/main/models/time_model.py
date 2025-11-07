from django.db import models

class Time(models.Model):
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.get_duration()}, {self.category}"
    
    class Meta:
        verbose_name = "Focus duration"
