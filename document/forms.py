from .models import *
from django.forms import TextInput
# noinspection PyUnresolvedReferences



RAZON_SOCIAL_CHOICES = (
    ('natural', 'Persona Natural'),
    ('juridica', 'Persona Jurídica'),
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
        widgets = {
            'cedula': forms.TextInput(attrs={'placeholder': 'V12345678'})
        }

class OrganizacionForm(forms.ModelForm):

    class Meta:

        model = DatosOrganizacion
        fields = '__all__'

        widgets = {
            'razon_social': forms.RadioSelect(choices=RAZON_SOCIAL_CHOICES),
            'rif': forms.TextInput(attrs={'placeholder': 'j-12345678-1'})
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

        widgets = {
            'cedula_eia': forms.TextInput(attrs={'placeholder': 'V12345678'}),
            'cedula_fisico': forms.TextInput(attrs={'placeholder': 'V12345678'}),
            'cedula_bio': forms.TextInput(attrs={'placeholder': 'V12345678'}),
            'cedula_eco': forms.TextInput(attrs={'placeholder': 'V12345678'}),
            'cedula_desa': forms.TextInput(attrs={'placeholder': 'V12345678'}),

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
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'datepicker'}),
        }


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
        fields = '__all__'
        labels = {
            'caracteristicas_suelo': 'Características',
            'sub_suelo': 'Subcaracterística',
            'atributos_suelo': 'Atributos',
            'comentarios_suelo': 'Comentarios',
        }

        widgets = {
            'caracteristicas_suelo': TextInput(attrs={'class': 'form-control'}),
            'sub_suelo': TextInput(attrs={'class': 'form-control'}),
            'atributos_suelo': TextInput(attrs={'class': 'form-control'}),
            'comentarios_suelo': TextInput(attrs={'class': 'form-control'}),
        }

class AguaForm(forms.ModelForm):
    class Meta:
        model = Agua
        fields = '__all__'
        labels = {
            'caracteristicas_agua': 'Características',
            'sub_agua': 'Subcaracterística',
            'atributos_agua': 'Atributos',
            'comentarios_agua': 'Comentarios',
        }

        widgets = {
            'caracteristicas_agua': TextInput(attrs={'class': 'form-control'}),
            'sub_agua': TextInput(attrs={'class': 'form-control'}),
            'atributos_agua': TextInput(attrs={'class': 'form-control'}),
            'comentarios_agua': TextInput(attrs={'class': 'form-control'}),
        }

class AireForm(forms.ModelForm):
    class Meta:
        model = Aire
        fields = '__all__'
        labels = {
            'caracteristicas_aire': 'Características',
            'sub_aire': 'Subcaracterística',
            'atributos_aire': 'Atributos',
            'comentarios_aire': 'Comentarios',
        }

        widgets = {
            'caracteristicas_aire': TextInput(attrs={'class': 'form-control'}),
            'sub_aire': TextInput(attrs={'class': 'form-control'}),
            'atributos_aire': TextInput(attrs={'class': 'form-control'}),
            'comentarios_aire': TextInput(attrs={'class': 'form-control'}),
        }

class ConclusionFisicoForm(forms.ModelForm):
    class Meta:
        model = ConclusionFisico
        fields = '__all__'
        labels = {
            'conclusion_fisico': 'Conclusiones',
        }

class ForestalForm(forms.ModelForm):
    class Meta:
        model = Forestal
        fields = '__all__'

        labels = {
            'caracteristicas_forestal': 'Características',
            'sub_forestal': 'Subcaracterística',
            'atributos_forestal': 'Atributos',
            'comentarios_forestal': 'Comentarios',
        }

        widgets = {
            'caracteristicas_forestal': TextInput(attrs={'class': 'form-control'}),
            'sub_forestal': TextInput(attrs={'class': 'form-control'}),
            'atributos_forestal': TextInput(attrs={'class': 'form-control'}),
            'comentarios_forestal': TextInput(attrs={'class': 'form-control'}),
        }

class FloraForm(forms.ModelForm):
    class Meta:
        model = Flora
        fields = '__all__'

        labels = {
            'caracteristicas_flora': 'Características',
            'sub_flora': 'Subcaracterística',
            'atributos_flora': 'Atributos',
            'comentarios_flora': 'Comentarios',
        }

        widgets = {
            'caracteristicas_flora': TextInput(attrs={'class': 'form-control'}),
            'sub_flora': TextInput(attrs={'class': 'form-control'}),
            'atributos_flora': TextInput(attrs={'class': 'form-control'}),
            'comentarios_flora': TextInput(attrs={'class': 'form-control'}),
        }

class FaunaForm(forms.ModelForm):
    class Meta:
        model = Fauna
        fields = '__all__'

        labels = {
            'caracteristicas_fauna': 'Características',
            'sub_fauna': 'Subcaracterística',
            'atributos_fauna': 'Atributos',
            'comentarios_fauna': 'Comentarios',
        }

        widgets = {
            'caracteristicas_fauna': TextInput(attrs={'class': 'form-control'}),
            'sub_fauna': TextInput(attrs={'class': 'form-control'}),
            'atributos_fauna': TextInput(attrs={'class': 'form-control'}),
            'comentarios_fauna': TextInput(attrs={'class': 'form-control'}),
        }

class ConclusionBiologicoForm(forms.ModelForm):
    class Meta:
        model = ConclusionBiologico
        fields = '__all__'
        labels = {
            'conclusion_bio': 'Conclusiones',
        }

class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = '__all__'
        labels = {
            'caracteristicas_social': 'Características',
            'sub_social': 'Subcaracterística',
            'atributos_social': 'Atributos',
            'comentarios_social': 'Comentarios',
        }

        widgets = {
            'caracteristicas_social': TextInput(attrs={'class': 'form-control'}),
            'sub_social': TextInput(attrs={'class': 'form-control'}),
            'atributos_social': TextInput(attrs={'class': 'form-control'}),
            'comentarios_social': TextInput(attrs={'class': 'form-control'}),
        }

class EconomicaForm(forms.ModelForm):
    class Meta:
        model = Economica
        fields = '__all__'
        labels = {
            'caracteristicas_eco': 'Características',
            'sub_economica': 'Subcaracterística',
            'atributos_eco': 'Atributos',
            'comentarios_eco': 'Comentarios',
        }

        widgets = {
            'caracteristicas_eco': TextInput(attrs={'class': 'form-control'}),
            'sub_economica': TextInput(attrs={'class': 'form-control'}),
            'atributos_eco': TextInput(attrs={'class': 'form-control'}),
            'comentarios_eco': TextInput(attrs={'class': 'form-control'}),
        }

class CulturalForm(forms.ModelForm):
    class Meta:
        model = Cultural
        fields = '__all__'
        labels = {
            'caracteristicas_cultural': 'Características',
            'sub_cultural': 'Subcaracterística',
            'atributos_cultural': 'Atributos',
            'comentarios_cultural': 'Comentarios',
        }

        widgets = {
            'caracteristicas_cultural': TextInput(attrs={'class': 'form-control'}),
            'sub_cultural': TextInput(attrs={'class': 'form-control'}),
            'atributos_cultural': TextInput(attrs={'class': 'form-control'}),
            'comentarios_cultural': TextInput(attrs={'class': 'form-control'}),
        }

class ConclusionCulturalForm(forms.ModelForm):
    class Meta:
        model = ConclusionCultural
        fields = '__all__'
        labels = {
            'conclusion_cultural': 'Conclusiones',
        }

class ActividadesForm(forms.ModelForm):
    class Meta:
        model = Actividades
        fields = '__all__'
        labels = {
         'proceso': 'Proceso',
         'actividad': 'Actividad',
         'amenazas': 'Amenazas',
          'vulnerabilidad': 'Vulnerabilidad',
        }

        widgets = {
            'proceso': TextInput(attrs={'class': 'form-control'}),
            'actividad': TextInput(attrs={'class': 'form-control'}),
            'amenazas': TextInput(attrs={'class': 'form-control'}),
            'vulnerabilidad': TextInput(attrs={'class': 'form-control'}),
        }

class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = '__all__'
        labels = {
            'comentarios': 'Comentarios',
        }

class DiagramaForm(forms.ModelForm):
    class Meta:
        model = Diagrama
        fields = '__all__'
        labels = {
            'archivo': 'Diagrama Gantt'
        }


class TalentoHumanoForm(forms.ModelForm):
    class Meta:
        model = TalentoHumano
        fields = '__all__'
        labels = {
            'actividad_talento': 'Actividad',
            'cantidad_talento': 'Cantidad',
            'tiempo_talento': 'Tiempo',
            'honorarios_talento': 'Honorarios',
            'total_talento': 'Total',
        }
        widgets = {
            'actividad_talento': TextInput(attrs={'class': 'form-control'}),
            'cantidad_talento': TextInput(attrs={'class': 'form-control'}),
            'tiempo_talento': TextInput(attrs={'class': 'form-control'}),
            'honorarios_talento': TextInput(attrs={'class': 'form-control', 'placeholder': '0,00'}),
            'total_talento':  TextInput(attrs={'class': 'form-control', 'placeholder': '0,00'}),
        }

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = '__all__'
        labels = {
            'actividad_servicios': 'Actividad',
            'cantidad_servicios': 'Cantidad',
            'tiempo_servicios': 'Tiempo',
            'monto_servicios': 'Monto Bs',
            'total_servicios': 'Total',
        }
        widgets = {
            'actividad_servicios': TextInput(attrs={'class': 'form-control'}),
            'cantidad_servicios': TextInput(attrs={'class': 'form-control'}),
            'tiempo_servicios': TextInput(attrs={'class': 'form-control'}),
            'monto_servicios': TextInput(attrs={'class': 'form-control', 'placeholder': '0,00'}),
            'total_servicios': TextInput(attrs={'class': 'form-control', 'placeholder': '0,00'}),
        }

class PasajesForm(forms.ModelForm):
    class Meta:
        model = Pasajes
        fields = '__all__'
        labels = {
            'actividad_pasajes': 'Actividad',
            'cantidad_pasajes': 'Cantidad',
            'tiempo_pasajes': 'Tiempo',
            'monto_pasajes': 'Monto Bs',
            'total_pasajes': 'Total',
        }
        widgets = {
            'actividad_pasajes': TextInput(attrs={'class': 'form-control'}),
            'cantidad_pasajes': TextInput(attrs={'class': 'form-control'}),
            'tiempo_pasajes': TextInput(attrs={'class': 'form-control'}),
            'monto_pasajes': TextInput(attrs={'class': 'form-control', 'placeholder': '0,00'}),
            'total_pasajes': TextInput(attrs={'class': 'form-control', 'placeholder': '0,00'}),
        }

class RecursosMaterialesForm(forms.ModelForm):
    class Meta:
        model = RecursosMateriales
        fields = '__all__'
        labels = {
            'materiales': 'Materiales',
            'cantidad_materiales': 'Cantidad',
            'control_materiales': 'C/U',
            'monto_materiales': 'Monto Bs',
            'total_materiales': 'Total',
        }
        widgets = {
            'materiales': TextInput(attrs={'class': 'form-control'}),
            'cantidad_materiales': TextInput(attrs={'class': 'form-control'}),
            'control_materiales': TextInput(attrs={'class': 'form-control'}),
            'monto_materiales': TextInput(attrs={'class': 'form-control', 'placeholder': '0,00'}),
            'total_materiales': TextInput(attrs={'class': 'form-control', 'placeholder': '0,00'}),
        }

class OficinaForm(forms.ModelForm):
    class Meta:
        model = Oficina
        fields = '__all__'
        labels = {
            'materiales_oficina': 'Materiales',
            'cantidad_oficina': 'Cantidad',
            'control_oficina': 'C/U',
            'monto_oficina': 'Monto Bs',
            'total_oficina': 'Total',
        }
        widgets = {
            'materiales_oficina': TextInput(attrs={'class': 'form-control'}),
            'cantidad_oficina': TextInput(attrs={'class': 'form-control'}),
            'control_oficina': TextInput(attrs={'class': 'form-control'}),
            'monto_oficina': TextInput(attrs={'class': 'form-control', 'placeholder': '0,00'}),
            'total_oficina': TextInput(attrs={'class': 'form-control', 'placeholder': '0,00'}),
        }

class InsumosForm(forms.ModelForm):
    class Meta:
        model = Insumos
        fields = '__all__'
        labels = {
            'insumos': 'Insumos',
            'cantidad_insumos': 'Cantidad',
            'control_insumos': 'C/U',
            'monto_insumos': 'Monto Bs',
            'total_insumos': 'Total',
        }
        widgets = {
            'insumos': TextInput(attrs={'class': 'form-control'}),
            'cantidad_insumos': TextInput(attrs={'class': 'form-control'}),
            'control_insumos': TextInput(attrs={'class': 'form-control'}),
            'monto_insumos': TextInput(attrs={'class': 'form-control', 'placeholder': '0,00'}),
            'total_insumos': TextInput(attrs={'class': 'form-control', 'placeholder': '0,00'}),
        }

class PlanInversionForm(forms.ModelForm):
    class Meta:
        model = PlanInversion
        fields = '__all__'
        labels = {
            'concepto': 'Concepto',
            'monto_plan': 'Monto Bs',
            'total_inversion': 'Total',
        }
        widgets = {
            'concepto': TextInput(attrs={'class': 'form-control'}),
            'monto_plan': TextInput(attrs={'class': 'form-control', 'placeholder': '0,00'}),
            'total_inversion': TextInput(attrs={'class': 'form-control', 'placeholder': '0,00'}),
        }

class InformacionForm(forms.ModelForm):
    class Meta:
        model = Informacion
        fields = '__all__'
        labels = {
            'informacion': 'Información',
        }

class ResponsableForm(forms.ModelForm):
    class Meta:
        model = Responsable
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'nivel_academico': 'Nivel Académico',
            'fecha': 'Fecha',
            'ciudad': 'Ciudad',
        }