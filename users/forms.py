from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=80)

    class Meta:
        # Change the User model on save.
        model = User

        # Order of fields in form.
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]
