from django.shortcuts import render
from django.contrib import messages
from my_utils import check_for_special_chars
from django.core.validators import validate_email


def login(request):
    return render(request, 'login.html')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'cadastro.html')

    full_name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')

    if not full_name or not email or not password or not confirm_password:
        messages.add_message(request, messages.ERROR, 'Erro: Todos os campos precisam ser preenchidos')
        return render(request, 'cadastro.html')

    if not check_for_special_chars(full_name):
        messages.add_message(request, messages.ERROR, 'Erro: O nome não pode conter espaços ou caracteres especiais')
        return render(request, 'cadastro.html')

    # TODO: terminar a view aqui

    full_name.strip()
    full_name = full_name.split(' ')

    first_name = full_name.pop(0)
    last_name = ' '.join(full_name)

    print(first_name, last_name)

    return render(request, 'login.html')
