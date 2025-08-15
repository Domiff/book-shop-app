from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView

from auth_app.forms import CreateUserForm


class RegisterUserView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = "auth_app/registration_app.html"
    success_url = reverse_lazy("auth_app:login")


class Login(LoginView):
    template_name = "auth_app/login_app.html"
    success_url = reverse_lazy("book_app:main")


class Logout(LogoutView):
    http_method_names = ["get", "post"]
    template_name = "auth_app/logout_app.html"
    next_page = reverse_lazy("book_app:main")
