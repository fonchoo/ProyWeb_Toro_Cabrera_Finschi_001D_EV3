from django.shortcuts import render
from .models import Registro

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


#************************* REGSITRO *******************************

def registroAdd(request):
    if request.method != "POST":
        registros = Registro.objects.all()
        context={'registros':registros}
        return render(request, 'test1/registro.html', context)
    else:
        email=request.POST["email"]
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        contraseña=request.POST["contraseña"]
        activo="1"

        obj=Registro.objects.create(email=email,
                                    nombre=nombre,
                                    apellido=apellido,
                                    contraseña=contraseña,
                                    activo=1)

        obj.save()
        context={'mensaje' : 'Datos guardados...'}
        return render(request, 'test1/registro.html', context)