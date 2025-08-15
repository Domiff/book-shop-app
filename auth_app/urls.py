from django.urls import path

from .views import Login, RegisterUserView, Logout

app_name = "auth_app"

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
]
