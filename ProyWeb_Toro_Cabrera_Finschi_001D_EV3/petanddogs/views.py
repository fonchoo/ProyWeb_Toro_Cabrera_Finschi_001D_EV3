from django.shortcuts import render
from .models import Categoria, Producto
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import UserEditForm
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    context={}
    return render(request,'petanddogs/index.html', context)

def formRegistro(request):
    context={}
    return render(request,'petanddogs/FormRegistro.html', context)

def perfil(request):
    context={}
    return render(request,'petanddogs/perfil.html', context)

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
#***************************** CRUD *************************************
@login_required
@permission_required('petanddogs.view_producto')
def crud(request):
    productos= Producto.objects.all()
    context={'productos':productos}
    return render(request, 'petanddogs/product_list.html',context)

@login_required
@permission_required('petanddogs.add_producto')
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
@login_required
@permission_required('petanddogs.delete_producto')
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
@login_required
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
    
@login_required
@permission_required('petanddogs.change_producto')
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

#***************************** REGISTRO *************************************
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
        return redirect('login')
    context={'mensaje' : 'Datos registrados...'}
    return render(request, 'petanddogs/login.html', context)

#***************************** LOGIN *************************************

def login_view(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('galeria')
            else:
                return render(request, 'login.html', {'error_message': 'Email o contraseña incorrectos'})
        except User.DoesNotExist:
            return render(request,'login.html', {'error_message': 'Email o contraseña incorrectos'})
    return render(request,'login.html')
#***************************** Editar perfil *************************************
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redirigir a la vista del perfil después de guardar
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'petanddogs/editar_perfil.html', {'form': form})

def exit(request):
    logout(request)
    return redirect('/')
