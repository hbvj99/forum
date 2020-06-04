from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from accounts.models import Profile


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Your last name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Your email address i.e. someone@domain.com'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Enter password again'})
        }


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class UserDetail(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Your last name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Your email address i.e. someone@domain.com'})
        }
