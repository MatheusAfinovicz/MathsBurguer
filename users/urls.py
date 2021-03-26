from django.urls import path
from .views import dashboard, create_adress, adresses

urlpatterns = [
    path('', dashboard),
    path('enderecos/', adresses),
    path('novo-endereco/', create_adress),
]
