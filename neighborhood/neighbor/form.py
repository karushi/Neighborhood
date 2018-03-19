from django import forms
from .models import user

class user (forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user']
