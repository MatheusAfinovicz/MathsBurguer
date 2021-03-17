from django.shortcuts import render


def home(request):
    return render(request, 'home/landingPage.html')


def login(request):
    return render(request, 'home/login.html')


def cadastro(request):
    return render(request, 'home/cadastro.html')
