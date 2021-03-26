from django.db import models
from django.contrib.auth.models import User
from django import forms


class UserAdress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    name = models.CharField(max_length=30, verbose_name='Nome')
    street = models.CharField(max_length=55, verbose_name='Rua')
    number = models.CharField(max_length=5, verbose_name='Número')
    district = models.CharField(max_length=30, verbose_name='Bairro')
    city = models.CharField(max_length=30, default='Guarapuava', verbose_name='Cidade')
    state = models.CharField(max_length=30, default='Paraná', verbose_name='Estado')
    complement = models.CharField(max_length=50, blank=True, verbose_name='Complemento')

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'


class FormAdress(forms.ModelForm):
    class Meta:
        model = UserAdress
        exclude = ('user',)
