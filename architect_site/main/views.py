from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'undevelop.html')

def contact(request):
    return render(request, 'contact.html')
