from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_view, name="home"),
    path("log_into_acc/", views.login_view, name="log_into_acc"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout/", views.logout_view, name="logout"),
]
