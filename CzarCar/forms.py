from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from CzarCar.models import Account, Rent, DrivingLicense

from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget

from mapwidgets.widgets import GooglePointFieldWidget


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, )

    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2')


class RentForm(ModelForm):
    class Meta:
        model = Rent
        fields = '__all__'


class EditDrivingLicenseForm(forms.ModelForm):

    class Meta:
        model = DrivingLicense
        fields = (
            'name','second_name','license_number','account')

    def __init__(self, *args, **kwargs):
        super(EditDrivingLicsenseForm, self).__init__(*args, **kwargs)
        self.fields['account'].required = False


