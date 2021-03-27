from django import forms
from .models import Messages


class FormMessage(forms.ModelForm):
    class Meta:
        model = Messages
        exclude = ('date',)
