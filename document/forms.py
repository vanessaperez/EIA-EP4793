from django import forms
from .models import *

RAZON_CHOICES = (
    ('pnatural', 'Natural'),
    ('pjuridica', 'Juridica'),
)

tierra_choices = (
            ('propia', 'Propia'),
            ('inti', 'I.N.T.I'),
            ('arrendada', 'Arrendada'),
            ('prestada', 'Prestada'),
)


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

    class Meta:

        model = DatosOrganizacion
        fields = ('razon_social', 'nombre', 'rif', 'dir_oficina', 'representante_legal', 'telefono', 'email')

        widgets = {
            'razon_social': forms.RadioSelect(choices=RAZON_CHOICES)
        }

        labels = {
            'razon_social': 'Razón Social',
            'nombre': 'Nombre',
            'rif': 'R.I.F',
            'dir_oficina': 'Dirección de Oficina',
            'representante_legal': 'Representante legal',
            'telefono': 'Teléfono',
            'email': 'E-mail'
        }

class DatosEspacioForm(forms.ModelForm):

    class Meta:

        model = DatosEspacio
        fields = ('tenencia_tierra', 'ubicacion')
        widgets = {
            'tenencia_tierra': forms.RadioSelect(choices=tierra_choices)
        }

        labels = {
            'tenencia_tierra': 'Tenencia de la Tierra',
            'ubicacion': 'Ubicación'
        }

class DatosLinderoForm(forms.ModelForm):
    class Meta:
        model = DatosLindero
        fields = ('lindero_norte', 'lindero_sur', 'lindero_este', 'lindero_oeste')
        labels = {
            'lindero_norte': 'Norte',
            'lindero_sur': 'Sur',
            'lindero_este': 'Este',
            'lindero_oeste': 'Oeste'
        }

class DatosCoordenadasForm(forms.ModelForm):
    class Meta:
        model = DatosCoordenadas
        fields = ('coor_norte', 'coor_sur','coor_este','coor_oeste')
        labels = {
            'coor_norte': 'Norte',
            'coor_sur': 'Sur',
            'coor_este': 'Este',
            'coor_oeste': 'Oeste'
        }