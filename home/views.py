from django.shortcuts import render, redirect
from .models import FormMessage
from django.contrib import messages
from utils.email_validator import email_validator
from utils.special_chars import check_for_special_chars


def index(request):
    return redirect('/home/')


def home(request):
    if request.method != 'POST':
        form = FormMessage()
        return render(request, 'landingPage.html', {'form': form})

    form = FormMessage(request.POST)

    if not form.is_valid():
        messages.add_message(request, messages.ERROR, 'Erro: Formulário inválido')
        form = FormMessage(request.POST)
        return render(request, 'landingPage.html', {'form': form})

    email = request.POST.get('email')

    if not email_validator(email):
        messages.add_message(request, messages.ERROR, 'Erro: E-mail inválido')
        form = FormMessage(request.POST)
        return render(request, 'landingPage.html', {'form': form})

    first_name = request.POST.get('first_name')

    if not check_for_special_chars(first_name) or ' ' in first_name:
        messages.add_message(request, messages.ERROR, 'Erro: O nome não pode conter espaços ou caracteres especiais')
        form = FormMessage(request.POST)
        return render(request, 'landingPage.html', {'form': form})

    last_name = request.POST.get('last_name')

    if not check_for_special_chars(last_name):
        messages.add_message(request, messages.ERROR, 'Erro: O sobrenome não pode conter caracteres especiais')
        form = FormMessage(request.POST)
        return render(request, 'landingPage.html', {'form': form})

    msg = request.POST.get('message')

    if len(msg) <= 10:
        messages.add_message(request, messages.ERROR, 'Erro: A mensagem precisa ter no mínimo 10 caracteres')
        form = FormMessage(request.POST)
        return render(request, 'landingPage.html', {'form': form})

    form.save()
    messages.add_message(request, messages.SUCCESS, 'Sucesso: Recebemos sua mensagem!')
    return redirect('/home/')
