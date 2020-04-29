from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Contact


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["work_title", "location", "bio", "work", "education"]
        widgets = {
            "work_title": forms.TextInput(
                attrs={"placeholder": "Enter your job title"}
            ),
            "location": forms.TextInput(attrs={"placeholder": "Enter your location"}),
            "bio": forms.Textarea(attrs={"placeholder": "About you", "rows": 10}),
            "education": forms.TextInput(
                attrs={"placeholder": "Your education background"}
            ),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter your name"}),
            "email": forms.TextInput(attrs={"placeholder": "mail@domain.com"}),
            "subject": forms.TextInput(attrs={"placeholder": "Subject"}),
            "message": forms.Textarea(attrs={"placeholder": "Message", "rows": 10}),
        }
