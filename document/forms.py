from django import forms
from django.forms import TextInput

from .models import *
from crispy_forms.helper import FormHelper, Layout

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
        fields = ('tenencia_tierra', 'ubicacion', 'lindero_norte', 'lindero_sur', 'lindero_este', 'lindero_oeste',
                  'coor_norte', 'coor_sur', 'coor_este', 'coor_oeste'
                  )
        widgets = {
            'tenencia_tierra': forms.RadioSelect(choices=tierra_choices)
        }

        labels = {
            'tenencia_tierra': 'Tenencia de la Tierra',
            'ubicacion': 'Ubicación',
            'lindero_norte': 'Norte',
            'lindero_sur': 'Sur',
            'lindero_este': 'Este',
            'lindero_oeste': 'Oeste',
            'coor_norte': 'Norte',
            'coor_sur': 'Sur',
            'coor_este': 'Este',
            'coor_oeste': 'Oeste'
        }


class DatosPersonalForm(forms.ModelForm):
    class Meta:
        model = DatosPersonal
        fields = (
            'nombre_eia', 'apellido_eia', 'cedula_eia', 'nivel_eia',
            'nombre_fisico', 'apellido_fisico', 'cedula_fisico', 'nivel_fisico',
            'nombre_bio', 'apellido_bio', 'cedula_bio', 'nivel_bio',
            'nombre_eco', 'apellido_eco', 'cedula_eco', 'nivel_eco',
            'nombre_desa', 'apellido_desa', 'cedula_desa', 'nivel_desa'
        )

        labels = {
            'nombre_eia': 'Nombre',
            'apellido_eia': 'Apellido',
            'cedula_eia': 'C.I. o Pasaporte',
            'nivel_eia': 'Nivel Académico',
            'nombre_fisico': 'Nombre',
            'apellido_fisico': 'Apellido',
            'cedula_fisico': 'C.I. o Pasaporte' ,
            'nivel_fisico': 'Nivel Académico',
            'nombre_bio': 'Nombre',
            'apellido_bio': 'Apellido',
            'cedula_bio': 'C.I. o Pasaporte',
            'nivel_bio': 'Nivel Académico',
            'nombre_eco': 'Nombre',
            'apellido_eco': 'Apellido',
            'cedula_eco': 'C.I. o Pasaporte',
            'nivel_eco': 'Nivel Académico',
            'nombre_desa': 'Nombre',
            'apellido_desa': 'Apellido',
            'cedula_desa': 'C.I. o Pasaporte',
            'nivel_desa': 'Nivel Académico'
        }


class DatosDocumentoForm(forms.ModelForm):
    class Meta:
        model = DatosDocumento
        fields = ('fecha', 'ciudad', 'estado', 'pais')
        labels = {
            'fecha': 'Fecha',
            'ciudad': 'Ciudad',
            'estado': 'Estado',
            'pais': 'País'
        }

        def __init__(self, *args, **kwargs):
            super(DatosDocumentoForm, self).__init__(*args, **kwargs)
            self.fields['fecha'].widget.attrs['class'] = 'datepicker'

class DescripcionProyectoForm(forms.ModelForm):
    class Meta:
        model = DescripcionProyecto
        fields = ('objetivo_general', 'objetivo_especifico', 'justificacion', 'imagen', 'marco')
        labels = {
            'objetivo_general': 'Objetivo General',
            'objetivo_especifico': 'Objetivos Específicos',
            'justificacion': 'Justificación e Importancia',
            'imagen': 'Zonificación del Área objeto de estudio',
            'marco': 'Marco Legal'
        }

class SueloForm(forms.ModelForm):
    class Meta:
        model = Suelo
        fields = ('caracteristicas', 'tipo_atributo', 'tipo_comentario', 'homo_atributo', 'homo_comentario',
                  'textura_atributo', 'textura_comentario')
        labels ={
            'caracteristicas': 'Características',
            'tipo_atributo' : 'Atributo',
            'tipo_comentario': 'Comentario',
            'homo_atributo': 'Atributo',
            'homo_comentario': 'Comentario',
            'textura_atributo':'Atributo',
            'textura_comentario': 'Comentario'
        }

        widgets = {
            'caracteristicas': TextInput(attrs={'placeholder': 'Sistema Edafológico'}),
        }

class AguaForm(forms.ModelForm):
    class Meta:
        model = Agua
        fields = ('caracteristicas', 'recurso_atributo', 'recurso_comentario', 'drenaje_atributo',
                'drenaje_comentario', 'corriente_atributo', 'corriente_comentario'
        )
        labels = {
            'caracteristicas': 'Características',
            'recurso_atributo': 'Atributo',
            'recurso_comentario': 'Comentario',
            'drenaje_atributo': 'Atributo',
            'drenaje_comentario': 'Comentario',
            'corriente_atributo': 'Atributo',
            'corriente_comentario': 'Comentario'
        }

class AireForm(forms.ModelForm):
    class Meta:
        model = Aire
        fields = ('caracteristicas', 'clima_atributo', 'clima_comentario', 'temp_atributo',
                'temp_comentario', 'vientos_atributo', 'vientos_comentario'
        )
        labels = {
            'caracteristicas': 'Características',
            'clima_atributo': 'Atributo',
            'clima_comentario': 'Comentario',
            'temp_atributo': 'Atributo',
            'temp_comentario': 'Comentario',
            'vientos_atributo': 'Atributo',
            'vientos_comentario': 'Comentario'
        }

class ConclusionFisicoForm(forms.ModelForm):
    class Meta:
        model = ConclusionFisico
        fields = ('conclusiones',)

class ForestalForm(forms.ModelForm):
    class Meta:
        model = Forestal
        fields = (
        'caracteristicas', 'especies_atributo', 'especies_comentario', 'conservacion_atributo',
        'conservacion_comentario', 'paisaje_atributo', 'paisaje_comentario', 'bosque_atributo',
        'bosque_comentario',
        )

        labels = {
            'caracteristicas': 'Características',
            'especies_atributo': 'Atributo',
            'especies_comentario': 'Comentario',
            'conservacion_atributo': 'Atributo',
            'conservacion_comentario': 'Comentario',
            'paisaje_atributo': 'Atributo',
            'paisaje_comentario': 'Comentario',
            'bosque_atributo': 'Atributo',
            'bosque_comentario': 'Comentario',
        }

        widgets = {
            'caracteristicas': TextInput(attrs={'placeholder': 'Forestal'}),
        }

class FloraForm(forms.ModelForm):
    class Meta:
        model = Flora
        fields = (
        'caracteristicas', 'coniferas_atributo', 'coniferas_comentario', 'xerofilas_atributo',
        'xerofilas_comentario', 'espeletias_atributo', 'espeletias_comentario',
        )

        labels = {
            'caracteristicas': 'Características',
            'coniferas_atributo': 'Atributo',
            'coniferas_comentario': 'Comentario',
            'xerofilas_atributo': 'Atributo',
            'xerofilas_comentario': 'Comentario',
            'espeletias_atributo': 'Atributo',
            'espeletias_comentario': 'Comentario',
        }

        widgets = {
            'caracteristicas': TextInput(attrs={'placeholder': 'Flora'}),
        }

class FaunaForm(forms.ModelForm):
    class Meta:
        model = Fauna
        fields = (
        'caracteristicas', 'mamiferos_atributo', 'mamiferos_comentario', 'peces_atributo',
        'peces_comentario', 'aves_atributo', 'aves_comentario', 'reptiles_atributo', 'reptiles_comentario',
        )

        labels = {
            'caracteristicas': 'Características',
            'mamiferos_atributo': 'Atributo',
            'mamiferos_comentario': 'Comentario',
            'peces_atributo': 'Atributo',
            'peces_comentario': 'Comentario',
            'aves_atributo': 'Atributo',
            'aves_comentario': 'Comentario',
            'reptiles_atributo': 'Atributo',
            'reptiles_comentario': 'Comentario',
        }

        widgets = {
            'caracteristicas': TextInput(attrs={'placeholder': 'Fauna'}),
        }

class ConclusionBiologicoForm(forms.ModelForm):
    class Meta:
        model = ConclusionBiologico
        fields = ('conclusiones',)