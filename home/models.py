from django.db import models
from django.utils import timezone
from django import forms


class MessageBox(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    message = models.TextField(max_length=1500)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.first_name}, {self.email}'


class FormMessageBox(forms.ModelForm):
    class Meta:
        model = MessageBox
        exclude = ('date',)
