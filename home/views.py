from django.shortcuts import render, redirect
from .models import FormMessageBox
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def index(request):
    return redirect('/home/')


def home(request):
    if request.method != 'POST':
        form = FormMessageBox()
        return render(request, 'landingPage.html', {'form': form})

    form = FormMessageBox(request.POST)

    if not form.is_valid():
        form = FormMessageBox(request.POST)
        return render(request, 'landingPage.html', {'form': form})

    email = request.POST.get('email')

    try:
        validate_email(email)

    except ValidationError:
        form = FormMessageBox(request.POST)
        return render(request, 'landingPage.html', {'form': form})

    form.save()
    return redirect('/home/')
