from django.db import models

class ProfileModel(models.Model):
    username = models.CharField(max_length=150, unique=True)
    github_username = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username