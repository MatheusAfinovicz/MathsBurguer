from django.urls import path
from .views import create_adress, adresses

urlpatterns = [
    path('enderecos/', adresses, name='adresses'),
    path('novo-endereco/', create_adress, name='new_adresses'),
]
