from django import forms
from .models import UserAdress


class FormAdress(forms.ModelForm):
    class Meta:
        model = UserAdress
        exclude = ('user',)
