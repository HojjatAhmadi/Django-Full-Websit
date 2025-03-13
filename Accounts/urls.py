from django.contrib import admin
from django.urls import path
from .views import  LoginView, RegisterView, ProfileView, ProfileCartView

app_name = "accounts"

urlpatterns = [
    path("login/" , LoginView.as_view() , name="login_form_accounts"),
    path("register/" , RegisterView.as_view() , name="register_form_accounts"),
    path("profile/", ProfileView.as_view(), name="profile_accounts"),
    path("profile/cart/", ProfileCartView.as_view(), name="profile_cart_accounts"),
]
