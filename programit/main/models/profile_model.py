from django.db import models

class ProfileModel(models.Model):
    username = models.CharField(max_length=150, unique=True)
    avatar_url = models.ImageField('img', upload_to='path/', blank=True, null=True)
    github_username = models.CharField(max_length=150, unique=True, null=True)
    description = models.TextField(blank=True)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, default=None)
    points = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username