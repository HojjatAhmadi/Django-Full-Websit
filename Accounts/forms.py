from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import User, Profile


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
