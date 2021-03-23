from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from my_utils import check_for_special_chars, email_validator


def login(request):
    return render(request, 'login.html')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'cadastro.html')

    full_name = request.POST.get('full_name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')

    if not full_name or not email or not password or not confirm_password:
        messages.add_message(request, messages.ERROR, 'Erro: Todos os campos precisam ser preenchidos')
        return render(request, 'cadastro.html', {'full_name': full_name, 'email': email})

    full_name.strip()
    full_name = full_name.upper()
    full_name = full_name.split(' ')

    for name in full_name:
        if not check_for_special_chars(name):
            messages.add_message(request, messages.ERROR, 'Erro: O nome não pode conter caracteres especiais '
                                                          'ou espaços sobrando')
            return render(request, 'cadastro.html', {'full_name': full_name, 'email': email})

    first_name = full_name.pop(0)
    last_name = ' '.join(full_name)

    if not last_name:
        messages.add_message(request, messages.ERROR, 'Erro: Escreva seu sobrenome, por favor')
        return render(request, 'cadastro.html', {'full_name': full_name, 'email': email})

    if not email_validator(email):
        messages.add_message(request, messages.ERROR, 'Erro: Email inválido')
        return render(request, 'cadastro.html', {'full_name': full_name, 'email': email})

    if len(password) < 6:
        messages.add_message(request, messages.ERROR, 'Erro: Sua senha deve ter pelo menos 6 caracteres')
        return render(request, 'cadastro.html', {'full_name': full_name, 'email': email})

    if password != confirm_password:
        messages.add_message(request, messages.ERROR, 'Erro: As senhas diferem')
        return render(request, 'cadastro.html', {'full_name': full_name, 'email': email})

    if User.objects.filter(email=email).exists():
        messages.add_message(request, messages.ERROR, 'Erro: Email já cadastrado')
        return render(request, 'cadastro.html', {'full_name': full_name, 'email': email})

    user = User.objects.create_user(username=email, email=email, password=password,
                                    first_name=first_name, last_name=last_name)
    user.save()

    messages.add_message(request, messages.SUCCESS, 'Conta criada com sucesso!')
    return redirect(login)
