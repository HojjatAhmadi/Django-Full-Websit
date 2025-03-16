from django.urls import path
from .views import  LoginView, RegisterView, ProfileView, ProfileCartView, UpdateUserInfoView1, \
    ChangePasswordView, UpdateUserInfoView2

app_name = "accounts"

urlpatterns = [
    path("login/" , LoginView.as_view() , name="login_form_accounts"),
    path("register/" , RegisterView.as_view() , name="register_form_accounts"),
    path("profile/", ProfileView.as_view(), name="profile_accounts"),
    path("profile/cart/", ProfileCartView.as_view(), name="profile_cart_accounts"),
    path("update/", UpdateUserInfoView1.as_view(), name="update_user_info"),
    path("password/update/", ChangePasswordView.as_view(), name="password_update"),
    path('update/profile/', UpdateUserInfoView2.as_view(), name='update_profile'),
]
