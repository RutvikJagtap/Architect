from django.shortcuts import render
from django.http import HttpResponse
from .models import portfolio as portfolio1

def Home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    category = request.GET.get('category')
    if category:
        projects = portfolio1.find({'category': category})
    else:
        projects = portfolio1.find()
    return render(request, 'portfolio.html', {'projects': projects})

def contact(request):
    return render(request, 'contact.html')

