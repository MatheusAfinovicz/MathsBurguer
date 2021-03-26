from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from utils.email_validator import email_validator
from utils.special_chars import check_for_special_chars
from home.views import home
from django.contrib.auth.decorators import login_required
from .models import FormAdress, UserAdress


def login(request):
    if request.method != 'POST':
        if request.user.is_authenticated:
            messages.add_message(request, messages.SUCCESS, f'Você já está logado como '
                                                            f'{request.user.first_name} {request.user.last_name}!')
            return redirect(dashboard)
        return render(request, 'login.html')

    email = request.POST.get('email')
    password = request.POST.get('password')

    if not email or not password:
        messages.add_message(request, messages.ERROR, 'Erro: Preencha todos os campos')
        return render(request, 'login.html')

    user = auth.authenticate(request, username=email, password=password)

    if not user:
        messages.add_message(request, messages.ERROR, 'Erro: Email ou Senha incorretos')
        return render(request, 'login.html')

    auth.login(request, user)
    messages.add_message(request, messages.SUCCESS, 'Logado com Sucesso!')
    return redirect(dashboard)


def cadastro(request):
    if request.method != 'POST':
        if request.user.is_authenticated:
            messages.add_message(request, messages.ERROR, f'Você está logado como '
                                                          f'{request.user.first_name} {request.user.last_name}! '
                                                          f'Faça Logout primeiro')
            return redirect(dashboard)
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


def logout(request):
    auth.logout(request)
    return redirect(home)


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required(login_url='/login/')
def adresses(request):
    user_adresses = UserAdress.objects.filter(
        user=request.user
    )
    return render(request, 'adresses.html', {'adresses': user_adresses})


@login_required(login_url='/login/')
def create_adress(request):
    if request.method != 'POST':
        form = FormAdress()
        return render(request, 'new_adress.html', {'form': form})

    form = FormAdress(request.POST)

    if not form.is_valid():
        messages.add_message(request, messages.ERROR, 'Erro: Formulário inválido')
        form = FormAdress(request.POST)
        return render(request, 'new_adress.html', {'form': form})

    adress = form.save(commit=False)
    adress.user = request.user
    adress.save()
    messages.add_message(request, messages.SUCCESS, 'Novo endereço adicionado com sucesso')

    return redirect(adresses)
