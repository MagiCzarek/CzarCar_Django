from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from CzarCar.models import Account, Rent

from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget

from mapwidgets.widgets import GooglePointFieldWidget


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100,)
    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2')

class RentForm(ModelForm):
    class Meta:
        model = Rent
        fields = '__all__'


