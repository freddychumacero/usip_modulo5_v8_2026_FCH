from django.http import HttpResponse
from django.shortcuts import render

from .models import Categoria


def index(request):
    return HttpResponse("Hola mundo")

def contact(request, name):
    return HttpResponse(f"Hola {name} bienvenido a la clase de Django")

def categorias(request):
    nombre_filtro = request.GET.get('nombre')
    
    if nombre_filtro:
        categorias = Categoria.objects.filter(nombre__icontains=nombre_filtro)
    else:
        categorias = Categoria.objects.all()
        
    return render(request, 'categorias.html', {
        "categorias": categorias,
        "filtro_actual": nombre_filtro
    })
