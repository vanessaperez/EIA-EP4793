from django import forms
from .models import *

class DatosProyectoForm(forms.ModelForm):

    class Meta:
        model = DatosProyecto
        fields = ('titulo', 'ubicacion', 'area', 'tipo')

class SolicitanteForm(forms.ModelForm):

    class Meta:
        model = DatosSolicitante
        fields = ('nombre', 'apellido', 'cedula', 'telefono', 'email')

class OrganizacionForm(forms.ModelForm):
    razon_social = forms.ChoiceField(choices=RAZON_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = DatosOrganizacion
        fields = ('razon_social', 'nombre', 'rif', 'dir_oficina', 'representante_legal', 'telefono', 'email')
