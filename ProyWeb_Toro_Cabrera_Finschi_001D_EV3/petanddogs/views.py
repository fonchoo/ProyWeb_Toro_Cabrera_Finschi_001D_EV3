from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Contacto
from .forms import ContactoForm 

# Create your views here.
def index(request):
    context={}
    return render(request,'petanddogs/index.html', context)

def formRegistro(request):
    context={}
    return render(request,'petanddogs/FormRegistro.html', context)

def iniciarSesion(request):
    context={}
    return render(request,'petanddogs/iniciarSesion.html', context)

def quiensessomos(request):
    context={}
    return render(request,'petanddogs/quienessomos.html', context)

def galeria(request):
    context={}
    return render(request,'petanddogs/galeria.html', context)

def adopcion(request):
    context={}
    return render(request,'petanddogs/adopcion.html', context)

def razas(request):
    context={}
    return render(request, 'petanddogs/razas.html', context)

def formContacto(request):
    context={}
    return render(request, 'petanddogs/formulariocontacto.html', context)

def calculadora(request):
    context={}
    return render(request, 'petanddogs/calculadora.html', context)

def lindoCat(request):
    context={}
    return render(request,'petanddogs/LindoCat.html', context)

def acana(request):
    context={}
    return render(request, 'petanddogs/Acana.html', context)

def naturea(request):
    context={}
    return render(request, 'petanddogs/Naturea.html', context)

def diamond(request):
    context={}
    return render(request, 'petanddogs/Diamond.html', context)

def orijen(request):
    context={}
    return render(request, 'petanddogs/Orijen.html', context)

def taste(request):
    context={}
    return render(request, 'petanddogs/Taste.html', context)


def guardar_contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        mail = request.POST.get('mail')
        mensaje = request.POST.get('mensaje')

        contacto_nuevo = Contacto(nombre=nombre, apellido=apellido, mail=mail, mensaje=mensaje)
        contacto_nuevo.save()

        return HttpResponseRedirect(reverse('index'))  # Redirigir a la página principal o donde sea

    return render(request, 'petanddogs/index.html') 