from django import forms

from .models import EurovisionCelebrities


class CelebritiesForm(forms.ModelForm):
    class Meta:
        model = EurovisionCelebrities
        fields = '__all__'
