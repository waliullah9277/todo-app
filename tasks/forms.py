from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task
from django.contrib.auth.models import User
from .models import Profile

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']  # <-- Add description here
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded w-full px-3 py-2',
                'placeholder': 'Enter task title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'border border-gray-300 rounded w-full px-3 py-2',
                'placeholder': 'Enter task details',
                'rows': 2,
            }),
        }
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'border border-gray-300 rounded w-full px-3 py-2',
                'placeholder': 'Write something about yourself',
                'rows': 3
            }),
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "border px-2 py-1 rounded w-full"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "border px-2 py-1 rounded w-full"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "border px-2 py-1 rounded w-full"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "border px-2 py-1 rounded w-full"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class": "border border-gray-300 rounded w-full px-3 py-2 focus:outline-none focus:ring focus:border-blue-400",
        "placeholder": "Enter your email"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "border border-gray-300 rounded w-full px-3 py-2 focus:outline-none focus:ring focus:border-blue-400",
        "placeholder": "Choose a username"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "border border-gray-300 rounded w-full px-3 py-2 focus:outline-none focus:ring focus:border-blue-400",
        "placeholder": "Create a password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "border border-gray-300 rounded w-full px-3 py-2 focus:outline-none focus:ring focus:border-blue-400",
        "placeholder": "Confirm your password"
    }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter your username',
            'class': 'border border-gray-300 rounded w-full px-3 py-2 focus:outline-none focus:ring focus:border-blue-400'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Enter your password',
            'class': 'border border-gray-300 rounded w-full px-3 py-2 focus:outline-none focus:ring focus:border-blue-400'
        })


class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'block w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-blue-500 bg-gray-50 text-gray-800 placeholder-gray-400',
            'placeholder': 'you@example.com'
        })
    )