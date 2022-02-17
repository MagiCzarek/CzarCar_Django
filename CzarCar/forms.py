from django import forms
from django.contrib.auth.forms import UserCreationForm
from CzarCar.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100,)
    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2')