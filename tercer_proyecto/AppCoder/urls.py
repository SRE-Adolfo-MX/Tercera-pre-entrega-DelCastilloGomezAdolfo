from django.urls import path
from AppCoder.views import show_html
from AppCoder.views import crear_publicacion_form, busqueda_usuario, mostrar_usuarios, mostrar_publicaciones, busqueda_publicacion

urlpatterns = [
    path("show/", show_html),
    path("crear_publicacion/", crear_publicacion_form),
    path("busqueda_usuario/", busqueda_usuario),
    path("usuarios/", mostrar_usuarios),
    path("publicaciones/", mostrar_publicaciones),
    path("busqueda_publicacion/", busqueda_publicacion),
]