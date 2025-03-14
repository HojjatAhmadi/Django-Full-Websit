from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import views as auth_views
from django.views.generic import View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm, RegisterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Profile, User
from Products.models import CartProduct
from django.contrib.auth import login, logout
from django.urls import reverse_lazy


# Create your views here.
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "Accounts/login_form_accounts.html"


class RegisterView(View):
    form_class = RegisterForm
    template_name = "Accounts/register_form_accounts.html"

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        data = request.POST
        form = self.form_class(data)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                user = User.objects.create_user(email=form.cleaned_data['email'],
                                                username=form.cleaned_data['username'],
                                                password=form.cleaned_data['password1'])
                Profile.objects.create(user=user)
                login(request, user)
                messages.success(request, f"Account created successfully, Welcome {form.cleaned_data['username']}",
                                 "success")
                return redirect("accounts:profile_accounts")
            else:
                messages.error(request, "Passwords do not match", "danger")
                return render(request, self.template_name, {"form": self.form_class})
        return render(request, self.template_name, {"form": self.form_class})


class ProfileView(View):
    template_name = "Accounts/profile_info_accounts.html"

    def get(self, request):
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        return render(request, self.template_name, {"profile": profile})


class ProfileCartView(View):
    template_name = "Accounts/profile_cart_accounts.html"

    def get(self, request):
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        carts = CartProduct.objects.filter(user=self.request.user)
        return render(self.request, self.template_name, {"carts": carts, "profile": profile})


class UpdateUserInfoView1(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name = "Accounts/update_info_accounts.html"
    success_url = reverse_lazy("accounts:profile_accounts")
    success_message = "User Information Update Successful!"

    def get_object(self, queryset=None):
        return get_object_or_404(User, username=self.request.user)


class ChangePasswordView(SuccessMessageMixin,auth_views.PasswordChangeView):
    success_message = "Password Change Successfully!"
    template_name = "Accounts/password_change.html"
    success_url = reverse_lazy("accounts:profile_accounts")