from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_user, name="logout"),
    path("forgot_password/", views.forgot_password_view, name="forgot_password"),
]