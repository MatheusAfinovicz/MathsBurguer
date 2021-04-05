from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Products


@login_required(login_url='/login/')
def dashboard(request):
    promotions = Products.objects.filter(
        promotion=True
    )

    sandwiches = Products.objects.filter(
        promotion=False,
        category__name='Lanches'
    )

    return render(request, 'dashboard.html', {'promotions': promotions, 'sandwiches': sandwiches})
