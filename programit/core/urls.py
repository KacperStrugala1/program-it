from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomeView.as_view(), name="home"),
    path("log_into_acc/", views.LoginView.as_view(), name="log_into_acc"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
]
