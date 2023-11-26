from django import forms

class UsuarioForms(forms.Form):
    nombreUsuario = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    comentario = forms.CharField()
    # fecha = forms.DateField()
    equipo1 = forms.CharField()
    equipo2 = forms.CharField()

class BusquedaUsuarioForms(forms.Form):
    idUsuario = forms.CharField()


class BusquedaPublicacionForms(forms.Form):
    nombreUsuario = forms.CharField()
