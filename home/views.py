from django.shortcuts import render, redirect
from .models import FormMessageBox
from django.contrib import messages
from my_utils import check_for_special_chars, email_validator


def index(request):
    return redirect('/home/')


def home(request):
    if request.method != 'POST':
        form = FormMessageBox()
        return render(request, 'landingPage.html', {'form': form})

    form = FormMessageBox(request.POST)

    if not form.is_valid():
        messages.add_message(request, messages.ERROR, 'Erro: Formulário inválido')
        form = FormMessageBox(request.POST)
        return render(request, 'landingPage.html', {'form': form})

    email = request.POST.get('email')

    if not email_validator(email):
        messages.add_message(request, messages.ERROR, 'Erro: E-mail inválido')
        form = FormMessageBox(request.POST)
        return render(request, 'landingPage.html', {'form': form})

    first_name = request.POST.get('first_name')

    if not check_for_special_chars(first_name) or ' ' in first_name:
        messages.add_message(request, messages.ERROR, 'Erro: O nome não pode conter espaços ou caracteres especiais')
        form = FormMessageBox(request.POST)
        return render(request, 'landingPage.html', {'form': form})

    last_name = request.POST.get('last_name')

    if not check_for_special_chars(last_name):
        messages.add_message(request, messages.ERROR, 'Erro: O sobrenome não pode conter caracteres especiais')
        form = FormMessageBox(request.POST)
        return render(request, 'landingPage.html', {'form': form})

    msg = request.POST.get('message')

    if len(msg) <= 10:
        messages.add_message(request, messages.ERROR, 'Erro: A mensagem precisa ter no mínimo 10 caracteres')
        form = FormMessageBox(request.POST)
        return render(request, 'landingPage.html', {'form': form})

    form.save()
    messages.add_message(request, messages.SUCCESS, 'Sucesso: Recebemos sua mensagem!')
    return redirect('/home/')
