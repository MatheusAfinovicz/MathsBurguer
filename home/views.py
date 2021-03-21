from django.shortcuts import render, redirect
from .models import FormMessageBox
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages


def index(request):
    return redirect('/home/')


def home(request):
    if request.method != 'POST':
        form = FormMessageBox()
        return render(request, 'landingPage.html', {'form': form})

    form = FormMessageBox(request.POST)

    if not form.is_valid():
        messages.add_message(request, messages.ERROR, 'Algo não é valido')
        form = FormMessageBox(request.POST)
        return render(request, 'landingPage.html', {'form': form})

    email = request.POST.get('email')

    try:
        validate_email(email)

    except ValidationError:
        messages.add_message(request, messages.ERROR, 'E-mail inválido')
        form = FormMessageBox(request.POST)
        return render(request, 'landingPage.html', {'form': form})

    form.save()
    messages.add_message(request, messages.SUCCESS, 'Recebemos sua mensagem!')
    return redirect('/home/')
