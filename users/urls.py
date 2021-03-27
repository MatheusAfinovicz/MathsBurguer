from django.urls import path
from .views import dashboard, create_adress, adresses

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('enderecos/', adresses, name='adresses'),
    path('novo-endereco/', create_adress, name='new_adresses'),
]
