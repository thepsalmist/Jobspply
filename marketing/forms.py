from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ["email"]
        widgets = {
            "email": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your email",
                    "rows": 50,
                }
            )
        }

