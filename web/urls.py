from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.decorators import  login_required
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home,name='home'),
    path('galeria/', views.galeria,name='galeria'),
    path('planes/', views.planes,name='planes'),
    path('quienes-somos/', views.about,name='quienes-somos'),
    path('registro.html', views.registro,name='registro'),
    path('registro2/', views.registro2,name='registro2'),
    path('usuario/',views.usuario,name="usuario" ),
    path('registro-mascota/', views.registro_mascota,name='registro_mascota'),
    path('listar/', views.listado_mascotas, name='listado_mascotas'),
    path('accounts/login/',views.Login.as_view(),name='login'),
    path('perfil',views.perfil,name='perfil'),
    path('logout/',login_required(views.logoutUsuario),name='logout'),
    path('registro/',views.RegistroUsuario.as_view(),name='registro'),
    url(r'^editar/(?P<rutMascota>\d+)/$',views.actualizar_mascota, name='editar_mascota'),
    url(r'^eliminar/(?P<rutMascota>\d+)/$',views.eliminiar_mascota, name='eliminar_mascota'),
    url(r'^historial-mascota/(?P<rutMascota>\d+)/$',views.historial_mascota, name='historial_mascota')

]