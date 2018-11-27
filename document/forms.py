from django import forms
from .models import *

class DatosProyectoForm(forms.ModelForm):

    class Meta:
        model = DatosProyecto
        fields = ('titulo', 'ubicacion', 'area', 'tipo')
        labels = {
            'titulo': 'Título del Proyecto',
            'ubicacion': 'Ubicación Geográfica',
            'area': 'Área de Desempeño',
            'tipo': 'Tipo de Proyecto'
        }

class SolicitanteForm(forms.ModelForm):

    class Meta:
        model = DatosSolicitante
        fields = ('nombre', 'apellido', 'cedula', 'telefono', 'email')
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'cedula': 'Cédula de Identidad',
            'telefono': 'Teléfono de Contacto',
            'email': 'E-mail'
        }

class OrganizacionForm(forms.ModelForm):
    razon_social = forms.ChoiceField(choices=RAZON_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = DatosOrganizacion
        fields = ('razon_social', 'nombre', 'rif', 'dir_oficina', 'representante_legal', 'telefono', 'email')
        labels = {
            'razon_social': 'Razón Social',
            'nombre': 'Nombre',
            'rif': 'R.I.F',
            'dir_oficina': 'Dirección de Oficina',
            'representante_legal': 'Representante legal',
            'telefono': 'Teléfono',
            'email': 'E-mail'
        }

