from django.shortcuts import render
from django.http import HttpResponse
from .models import Almacen


# Create your views here.

def index(request):
    return render (request, 'App/index.html')

def inicio(request):
    return render (request, 'App/inicio.html')

def almacen(request):
    return render(request, 'Areas/almacen.html')

def produccion(request):
    return render(request, 'Areas/produccion.html')

def calidad(request):
    return render(request, 'Areas/calidad.html')

def reportes(request):
    return render(request, 'App/reportes.html')




