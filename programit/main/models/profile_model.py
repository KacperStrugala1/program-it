from django.db import models

class ProfileModel(models.Model):
    username = models.CharField(max_length=150, unique=True)
    github_username = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, default=None)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username