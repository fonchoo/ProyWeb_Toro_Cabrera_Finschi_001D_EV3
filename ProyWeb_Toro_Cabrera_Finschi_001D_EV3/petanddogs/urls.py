from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index', views.index, name='index'),
    path('index/FormRegistro', views.formRegistro, name='FormRegistro'),
    path('FormRegistro/iniciarSesion',views.iniciarSesion, name='iniciarSesion'),
    path('index/quienessomos', views.quiensessomos, name='quienessomos'),
    path('index/galeria', views.galeria, name='galeria'),
    path('index/adopcion', views.adopcion, name='adopcion'),
    path('index/razas', views.razas, name='razas'),
    path('quienessomos/formContacto', views.formContacto, name='formContacto'),
    path('galeria/calculadora', views.calculadora, name='calculadora'),
    path('galeria/lindocat', views.lindoCat, name='lindocat'),
    path('galeria/acana', views.acana, name='acana'),
    path('galeria/naturea', views.naturea, name='naturea'),
    path('galeria/diamond', views.diamond, name='diamond'),
    path('galeria/orijen', views.orijen, name='orijen'),
    path('galeria/taste', views.taste, name='taste'),
    path('productos', views.productos, name='productos'),
    path('crud',views.crud,name='crud'),
    path('productosAdd', views.productosAdd, name='productosAdd'),
    path('productosUpdate', views.productosUpdate, name='productosUpdate'),
    path('productos_findEdit/<str:pk>', views.productos_findEdit, name='productos_findEdit'),
    path('productos_del/<str:pk>', views.productos_del, name='productos_del'),
]

