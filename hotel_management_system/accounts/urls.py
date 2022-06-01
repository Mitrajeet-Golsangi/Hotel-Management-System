from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path("register-as/", TemplateView.as_view(template_name="auth/sign_in_as.html"), name="register_as"),
    path("guest-register/", guest_register, name="guest_register"),
    path("staff-register/", staff_register, name="staff_register"),
    path("login/", signIn, name="login"),
    path("logout/", logout, name="logout"),
]
