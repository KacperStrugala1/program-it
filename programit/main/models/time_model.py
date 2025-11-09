from django.db import models

class Time(models.Model):
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    user_id = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Time "

class Category(models.Model):
    category = models.ManyToManyField(Time)
