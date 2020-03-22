from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your email",}
        ),
        label="",
    )

    class Meta:
        model = SignUp
        fields = ["email"]

