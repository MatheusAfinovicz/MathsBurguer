from django.db import models
from django.utils import timezone
from django import forms


class Messages(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Nome')
    last_name = models.CharField(max_length=100, verbose_name='Sobrenome')
    email = models.CharField(max_length=255, verbose_name='Email')
    message = models.TextField(max_length=1500, verbose_name='Mensagem')
    date = models.DateTimeField(default=timezone.now, verbose_name='Data de criação')

    def __str__(self):
        return f'{self.first_name}, {self.email}'

    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'


class FormMessage(forms.ModelForm):
    class Meta:
        model = Messages
        exclude = ('date',)
