from django.shortcuts import render
from .models import Usuario

def index_list(request):
    return render(request,
     'index.html',)

def contacto_list(request):
    return render(request, 
    'contacto.html', {}) 

def galeria_list(request):
    return render(request, 
    'galeria.html', {}) 

def planes_list(request):
    return render(request, 
    'planes.html', {})
