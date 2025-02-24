from django.contrib import admin
from django.urls import path
from .views import  LoginView, RegisterView

app_name = "accounts"

urlpatterns = [
    path("login/" , LoginView.as_view() , name="login_form_accounts"),
    path("register/" , RegisterView.as_view() , name="register_form_accounts"),
]
