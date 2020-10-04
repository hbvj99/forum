from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import Profile

User = get_user_model()


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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'Sorry, somebody already registered with this email address.')
        return email


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
