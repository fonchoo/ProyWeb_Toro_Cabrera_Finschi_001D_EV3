from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from django.views.decorators.csrf import csrf_protect



# Create your views here.
def index(request):
    context={}
    return render(request,'petanddogs/index.html', context)

def formRegistro(request):
    context={}
    return render(request,'registration/register.html', context)

def iniciarSesion(request):
    context={}
    return render(request,'registration/login.html', context)

def quiensessomos(request):
    context={}
    return render(request,'petanddogs/quienessomos.html', context)

@login_required
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


#************************* REGISTRO *******************************

def registroAdd(request):
    if request.method == "POST":
        email=request.POST["email"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        password=request.POST["password"]
        password_confirm=request.POST["password_confirm"]

        if CustomUser.objects.filter(email=email).exists():
            return render(request,'register.html',{'error_message':'El email ya esta registrado'})
        
        user=CustomUser.objects.create(email=email,
                                    first_name=first_name,
                                    last_name=last_name,
                                    password=make_password(password))

        user.save()
        login(request, user)
        return redirect('index')
    context={'mensaje' : 'Datos registrados...'}
    return render(request, 'registration/login.html', context)
    
#***************************** LOGIN **************************************
@csrf_protect
def login_exist(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'login.html', {'error_message': 'Email o contraseña incorrectos'})
        except User.DoesNotExist:
            return render(request,'login.html', {'error_message': 'Email o contraseña incorrectos'})
    return render(request,'login.html')



#***************************** LOGOUT *************************************
def exit(request):
    logout(request)
    return redirect('index')
