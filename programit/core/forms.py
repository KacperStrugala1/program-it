from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=150, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class TaskForm(forms.Form):
    task_name = forms.CharField(max_length=100)
    task_category = forms.CharField(max_length=50)
    task_description = forms.CharField(max_length=500)