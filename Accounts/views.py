from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views.generic import View
from .forms import LoginForm, RegisterForm

# Create your views here.
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "Accounts/login_form_accounts.html"

class RegisterView(View):
    form_class = RegisterForm
    template_name = "Accounts/register_form_accounts.html"

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

