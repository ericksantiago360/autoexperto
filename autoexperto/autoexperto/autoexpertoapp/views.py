from django.shortcuts import render
from django.http import HttpResponse
from .models import datosdelauto

# Create your views here.
def inicio(request):
    return render(request,'paginas/inicio.html')
def nosotros(request):
    return render(request,'paginas/nosotros.html')

def autos(request):
    autos = datosdelauto.objects.all()
    return render(request,'autos/index.html' ,{'autos': autos })

def crear(request):     
    return render(request,'autos/crear.html')
def editar(request):
    return render(request,'autos/editar.html')
def form(request):
    return render(request,'autos/form.html')



