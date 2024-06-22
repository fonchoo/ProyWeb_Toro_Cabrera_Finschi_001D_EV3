from django.shortcuts import render
from .models import Categoria, Producto, Registro
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django import forms
    
    
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

def crud(request):
    productos= Producto.objects.all()
    context={'productos':productos}
    return render(request, 'petanddogs/product_list.html',context)

def productosAdd(request):
    if request.method != "POST":
        categorias=Categoria.objects.all()
        context={'categorias':categorias}
        return render(request,'petanddogs/productos_add.html',context)
    else:
        id=request.POST["id"]
        nombre=request.POST["nombre"]
        descripcion=request.POST["descripcion"]
        imagen=request.FILES.get("imagen")
        precio=request.POST["precio"]
        stock=request.POST["stock"]
        categoria=request.POST["categoria"]       
                
        objCategoria=Categoria.objects.get(idCategoria = categoria)
        obj=Producto.objects.create(id_producto=id,
                                  nombre=nombre,
                                  descripcion=descripcion,
                                  imagen=imagen,
                                  precio=precio,
                                  stock=stock,
                                  categoria=objCategoria,
                                  )
        obj.save()
        context={'mensaje':"Ok, datos grabados..."}
        return render(request,'petanddogs/productos_add.html',context)
    
def productos_del(request,pk):
    context={}
    try:
        producto=Producto.objects.get(id_producto=pk)
        
        producto.delete()
        mensaje="Bien, datos eliminados"
        productos= Producto.objects.all()
        context= {'productos': productos, 'mensajes': mensaje}
        return render(request,'petanddogs/product_list.html', context)
    except:
        mensaje="Error, rut no existe..."
        productos= Producto.objects.all()
        context={'productos':productos,'mensaje':mensaje}
        return render(request, 'petanddogs/product_list.html',context)
    
def productosUpdate(request):
    if  request.method =="POST":
        id=request.POST["id"]
        nombre=request.POST["nombre"]
        descripcion=request.POST["descripcion"]
        imagen=request.FILES.get("imagen")
        precio=request.POST["precio"]
        stock=request.POST["stock"]
        categoria=request.POST["categoria"]       
                
        objCategoria=Categoria.objects.get(idCategoria = categoria)
        
        producto=Producto()
        producto.id_producto=id
        producto.nombre=nombre
        producto.descripcion=descripcion
        if imagen:
            producto.imagen = imagen
        producto.precio=precio
        producto.stock=stock
        producto.categoria=objCategoria
        producto.save()
        
        categorias = Categoria.objects.all()
        context={'mensaje':"Ok, datos actualizados...",'categorias':categorias,'producto':producto}
        return render(request,'petanddogs/productos_edit.html',context)
    else:
        productos= Producto.objects.all()
        context={'productos':productos}
        return render(request, 'petanddogs/product_list.html', context)
    
    
def productos_findEdit(request,pk):
    if pk !="":
       producto=Producto.objects.get(id_producto=pk)
       categorias=Categoria.objects.all()
       
       print(type(producto.categoria))
       
       context={'producto':producto,'categorias':categorias}
       if producto:
           return render(request,'petanddogs/productos_edit.html', context)
       else:
           context={'mensaje':"Error, id no existe..."}
           return render(request, 'petanddogs/product_list.html', context)
       
       

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
    
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            correo = form.cleaned_data.get('correo')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=correo, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Sesión Iniciada! Vuelva a navegar.')
                return redirect('index')  # redirige a la página principal u otra página
            else:
                messages.error(request, 'Correo o contraseña incorrectos.')
    return render(request, 'login.html', {'form': form})

class LoginForm(forms.Form):
    correo = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'formulario__input',
        'placeholder': 'correo@correo.com',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'formulario__input',
    }))




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('index')



