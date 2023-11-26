from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import Usuario, Publicacion, Partido
from AppCoder.forms import UsuarioForms, BusquedaUsuarioForms, BusquedaPublicacionForms
from datetime import datetime, date

# Create your views here.

def show_html(request):
    contexto = {
        "nombre": "Welcome",
    }
    return render(request, template_name="index.html", context=contexto)


def mostrar_usuarios(request):
    usuarios = Usuario.objects.all()
    contexto = {
        "usuarios": usuarios,
        "nombre": "Welcome",
        "form": BusquedaUsuarioForms()
    }
    return render(request, template_name="AppCoder/usuarios.html", context=contexto)

def crear_publicacion_form(request):
    if request.method == "POST":
        usuario_formulario = UsuarioForms(request.POST)
        if usuario_formulario.is_valid():
            informacion = usuario_formulario.cleaned_data
            usuario_crear = Usuario(nombreUsuario = informacion["nombreUsuario"], nombre = informacion["nombre"], apellido = informacion["apellido"], email = informacion["email"])
            partido_crear = Partido(equipo1 = informacion["equipo1"], equipo2 = informacion["equipo2"], fecha = date.today())
            publicacion_crear = Publicacion(nombreUsuario = informacion["nombreUsuario"], comentario = informacion["comentario"], fecha = date.today(), equipo1 = informacion["equipo1"], equipo2 = informacion["equipo2"])
            usuario_crear.save()
            partido_crear.save()
            publicacion_crear.save()
            return redirect("/app/show/")

    usuario_formulario = UsuarioForms()
    contexto = {
        "form": usuario_formulario
    }

    return render(request, template_name="AppCoder/crear_publicacion.html", context=contexto)


def busqueda_usuario(request):
    nombreUsuario = request.GET["idUsuario"]
    usuario = Usuario.objects.filter(nombreUsuario__icontains=nombreUsuario)
    contexto = {
        "usuarios": usuario,
        "form": BusquedaUsuarioForms(),
        "nombre": "Welcome"
    }

    return render(request, template_name="AppCoder/usuarios.html", context=contexto)

def mostrar_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    contexto = {
        "publicaciones": publicaciones,
        "nombre": "Welcome",
        "form": BusquedaUsuarioForms()
    }
    return render(request, template_name="AppCoder/publicaciones.html", context=contexto)

def busqueda_publicacion(request):
    nombreUsuario = request.GET["idUsuario"]
    publicacion = Publicacion.objects.filter(nombreUsuario__icontains=nombreUsuario)
    contexto = {
        "publicaciones": publicacion,
        "form": BusquedaUsuarioForms(),
        "nombre": "Welcome"
    }

    return render(request, template_name="AppCoder/publicaciones.html", context=contexto)