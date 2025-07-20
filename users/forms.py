from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["full_name", "username", "email", "password1", "password2"]