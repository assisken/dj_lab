from django import forms
from django.contrib.auth.models import User

from .models import EurovisionCelebrities


class CelebritiesForm(forms.ModelForm):
    class Meta:
        model = EurovisionCelebrities
        fields = '__all__'


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

    def form_valid(self):
        pass

    class Meta:
        model = User
        fields = ['username', 'password', 'password1', 'first_name', 'last_name', 'email']
        widgets = {
            'email': forms.EmailInput(),
            'password': forms.PasswordInput(),
        }
