from django import forms
from django.core.exceptions import ValidationError

from .models import *


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ('firstname', 'lastname', 'username', 'email', 'password')
        # widgets = {
        #     'firstname': forms.TextInput(attrs={'class': 'form-control my-5'}),
        #     'lastname': forms.TextInput(attrs={"class": "form-control mb-5"}),
        #     'username': forms.TextInput(attrs={"class": "form-control mb-5"}),
        #     'email': forms.TextInput(attrs={"class": "form-control mb-5"}),
        #     'password': forms.TextInput(attrs={"class": "form-control mb-5"}),
        # }
