from django import forms
from .models import Service


class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['icon', 'head', 'description']
