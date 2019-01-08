import re
from django.db import models
from django import forms
from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class DatosSolicitante(models.Model):

    nombre = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Nombre incorrecto'),
                'invalid')])

    apellido = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Apellido incorrecto'),
                'invalid')])

    cedula = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                re.compile('/^[V|E|J|P]-[0-9]{5,9}$/'),
                _('Cédula incorrecta'),
                'invalid')])


    telefono = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                (re.compile('^[0-9]{11}$')),
                _('Teléfono incorrecto'),
                'invalid')])
    email = models.CharField(max_length=30)

class DatosOrganizacion(models.Model):

    RAZON_SOCIAL_CHOICES = (
        ('natural', 'Persona Natural'),
        ('juridica', 'Persona Jurídica'),
    )

    natural = 'natural'

    nombre = models.CharField(max_length=60)
    razon_social = models.CharField(choices=RAZON_SOCIAL_CHOICES, default=natural, max_length=8)
    rif = models.CharField(
        max_length=12,
        unique=True,
        validators=[
            RegexValidator(
                re.compile('^([VEJPGvejpg]{1})-([0-9]{8})-([0-9]{1}$)'),
                _('RIF incorrecto'),
                'invalid')])
    dir_oficina = models.CharField(max_length=130)
    representante_legal = models.CharField(max_length=130)
    telefono = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                (re.compile('^[0-9]{11}$')),
                _('Teléfono incorrecto'),
                'invalid')])

    email = models.CharField(max_length=30)

class DatosEspacio(models.Model):

    tierra_choices = (
        ('propia', 'Propia'),
        ('inti', 'I.N.T.I'),
        ('arrendada', 'Arrendada'),
        ('prestada', 'Prestada'),
    )

    propia = 'Propia'

    tenencia_tierra = models.CharField(choices=tierra_choices, default=propia, max_length=100)
    ubicacion = models.CharField(max_length=300)
    lindero_norte = models.CharField(max_length=100)
    lindero_sur = models.CharField(max_length=100)
    lindero_este = models.CharField(max_length=100)
    lindero_oeste = models.CharField(max_length=100)
    coor_norte = models.CharField(max_length=100)
    coor_sur = models.CharField(max_length=100)
    coor_este = models.CharField(max_length=100)
    coor_oeste = models.CharField(max_length=100)


class DatosPersonal(models.Model):

    nombre_eia = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Nombre incorrecto'),
                'invalid')])
    apellido_eia = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Apellido incorrecto'),
                'invalid')])
    cedula_eia = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                re.compile('/^[V|E|J|P]-[0-9]{5,9}$/'),
                _('Cédula incorrecta'),
                'invalid')])
    nivel_eia = models.CharField(max_length=40)
    nombre_fisico = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Nombre incorrecto'),
                'invalid')])

    apellido_fisico = models.CharField(max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Apellido incorrecto'),
                'invalid')])
    cedula_fisico = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                re.compile('/^[V|E|J|P]-[0-9]{5,9}$/'),
                _('Cédula incorrecta'),
                'invalid')])
    nivel_fisico = models.CharField(max_length=40)
    nombre_bio = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Nombre incorrecto'),
                'invalid')])
    apellido_bio = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Apellido incorrecto'),
                'invalid')])
    cedula_bio = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                re.compile('/^[V|E|J|P]-[0-9]{5,9}$/'),
                _('Cédula incorrecta'),
                'invalid')])
    nivel_bio = models.CharField(max_length=40)
    nombre_eco = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Nombre incorrecto'),
                'invalid')])
    apellido_eco = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Apellido incorrecto'),
                'invalid')])
    cedula_eco = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                re.compile('/^[V|E|J|P]-[0-9]{5,9}$/'),
                _('Cédula incorrecta'),
                'invalid')])
    nivel_eco = models.CharField(max_length=40)
    nombre_desa = models.CharField(max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Nombre incorrecto'),
                'invalid')])
    apellido_desa = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Apellido incorrecto'),
                'invalid')])
    cedula_desa = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                re.compile('/^[V|E|J|P]-[0-9]{5,9}$/'),
                _('Cédula incorrecta'),
                'invalid')])
    nivel_desa = models.CharField(max_length=40)

class DatosDocumento(models.Model):
    fecha = models.DateField()
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

class DescripcionProyecto(models.Model):
    objetivo_general = models.TextField()
    objetivo_especifico = models.TextField()
    justificacion = models.TextField()
    imagen = models.ImageField(upload_to="static/img", null=True)
    marco = models.TextField()

class Suelo(models.Model):
    caracteristicas_suelo = models.CharField(max_length=100, blank=True)
    sub_suelo = models.CharField(max_length=100, blank=True)
    atributos_suelo = models.CharField(max_length=100, blank=True)
    comentarios_suelo = models.CharField(max_length=100, blank=True)


class Agua(models.Model):
    caracteristicas_agua = models.CharField(max_length=100, blank=True)
    sub_agua = models.CharField(max_length=100, blank=True)
    atributos_agua = models.CharField(max_length=100, blank=True)
    comentarios_agua = models.CharField(max_length=100,blank=True)

class Aire(models.Model):

    caracteristicas_aire = models.CharField(max_length=100, blank=True)
    sub_aire = models.CharField(max_length=100, blank=True)
    atributos_aire = models.CharField(max_length=100, blank=True)
    comentarios_aire = models.CharField(max_length=100, blank=True)

class ConclusionFisico(models.Model):
    conclusiones = models.TextField()

class Forestal(models.Model):
    caracteristicas_forestal = models.CharField(max_length=100, blank=True)
    sub_forestal = models.CharField(max_length=100, blank=True)
    atributos_forestal = models.CharField(max_length=100, blank=True)
    comentarios_forestal = models.CharField(max_length=100, blank=True)

class Flora(models.Model):
    caracteristicas_flora = models.CharField(max_length=100, blank=True)
    sub_flora = models.CharField(max_length=100, blank=True)
    atributos_flora = models.CharField(max_length=100, blank=True)
    comentarios_flora = models.CharField(max_length=100, blank=True)

class Fauna(models.Model):
    caracteristicas_fauna = models.CharField(max_length=100, blank=True)
    sub_fauna = models.CharField(max_length=100, blank=True)
    atributos_fauna = models.CharField(max_length=100, blank=True)
    comentarios_fauna = models.CharField(max_length=100, blank=True)

class ConclusionBiologico(models.Model):
    conclusiones = models.TextField()

class Social(models.Model):
    caracteristicas_social = models.CharField(max_length=100, blank=True)
    sub_social = models.CharField(max_length=100, blank=True)
    atributos_social = models.CharField(max_length=100, blank=True)
    comentarios_social = models.CharField(max_length=100, blank=True)

class Economica(models.Model):
    caracteristicas_eco = models.CharField(max_length=100, blank=True)
    sub_economica = models.CharField(max_length=100, blank=True)
    atributos_eco = models.CharField(max_length=100, blank=True)
    comentarios_eco = models.CharField(max_length=100, blank=True)

class Cultural(models.Model):
    caracteristicas_cultural = models.CharField(max_length=100, blank=True)
    sub_cultural = models.CharField(max_length=100, blank=True)
    atributos_cultural = models.CharField(max_length=100, blank=True)
    comentarios_cultural = models.CharField(max_length=100, blank=True)

class ConclusionCultural(models.Model):
    conclusion_cultural = models.TextField()

class Actividades(models.Model):
    proceso = models.CharField(max_length=100, blank=True)
    actividad = models.CharField(max_length=100, blank=True)
    amenazas = models.CharField(max_length=100, blank=True)
    vulnerabilidad = models.CharField(max_length=100, blank=True)

class Comentarios(models.Model):
    comentarios = models.TextField()

class Diagrama(models.Model):
    archivo = models.FileField(upload_to='static/files')

class TalentoHumano(models.Model):
    actividad_talento = models.CharField(max_length=100, blank=True)
    cantidad_talento = models.CharField(max_length=100, blank=True)
    tiempo_talento = models.CharField(max_length=100, blank=True)
    honorarios_talento = models.CharField(max_length=100, blank=True)
    total_talento = models.CharField(max_length=100, blank=True)

class Servicios(models.Model):
    actividad_servicios = models.CharField(max_length=100, blank=True)
    cantidad_servicios = models.CharField(max_length=100, blank=True)
    tiempo_servicios = models.CharField(max_length=100, blank=True)
    monto_servicios = models.CharField(max_length=100, blank=True)
    total_servicios = models.CharField(max_length=100, blank=True)

class Pasajes(models.Model):
    actividad_pasajes = models.CharField(max_length=100, blank=True)
    cantidad_pasajes = models.CharField(max_length=100, blank=True)
    tiempo_pasajes = models.CharField(max_length=100, blank=True)
    monto_pasajes = models.CharField(max_length=100, blank=True)
    total_pasajes = models.CharField(max_length=100, blank=True)

class RecursosMateriales(models.Model):
    materiales = models.CharField(max_length=100, blank=True)
    cantidad_materiales = models.CharField(max_length=100, blank=True)
    control_materiales = models.CharField(max_length=100, blank=True)
    monto_materiales = models.CharField(max_length=100, blank=True)
    total_materiales = models.CharField(max_length=100, blank=True)

class Oficina(models.Model):
    materiales_oficina = models.CharField(max_length=100, blank=True)
    cantidad_oficina = models.CharField(max_length=100, blank=True)
    control_oficina = models.CharField(max_length=100, blank=True)
    monto_oficina = models.CharField(max_length=100, blank=True)
    total_oficina = models.CharField(max_length=100, blank=True)

class Insumos(models.Model):
    insumos = models.CharField(max_length=100, blank=True)
    cantidad_insumos = models.CharField(max_length=100, blank=True)
    control_insumos = models.CharField(max_length=100, blank=True)
    monto_insumos = models.CharField(max_length=100, blank=True)
    total_insumos = models.CharField(max_length=100, blank=True)

class PlanInversion(models.Model):
    concepto = models.CharField(max_length=100, blank=True)
    monto_plan = models.CharField(max_length=100, blank=True)
    total_inversion = models.CharField(max_length=100, blank=True)

class Informacion(models.Model):
    informacion = models.TextField()

class Responsable(models.Model):
    nombre = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Nombre incorrecto'),
                'invalid')])

    apellido = models.CharField(
        max_length=60,
        validators=[
            RegexValidator(
                re.compile(r'^[\w+\s]+$'),
                _('Apellido incorrecto'),
                'invalid')])
    nivel_academico = models.CharField(max_length=100)
    fecha = models.DateField()
    ciudad = models.CharField(max_length=100)


class DatosProyecto(models.Model):
    titulo = models.CharField(max_length=130)
    ubicacion = models.CharField(max_length=130)
    area = models.CharField(max_length=130)
    tipo = models.CharField(max_length=130)
    status = models.CharField(max_length=20, default='Pendiente')
    solicitante = models.ForeignKey(DatosSolicitante, null=True, on_delete=models.CASCADE)
    organizacion = models.ForeignKey(DatosOrganizacion, null=True, on_delete=models.CASCADE)
    d_espacio = models.ForeignKey(DatosEspacio, null=True, on_delete=models.CASCADE)
    d_personal = models.ForeignKey(DatosPersonal, null=True, on_delete=models.CASCADE)
    d_documento = models.ForeignKey(DatosDocumento, null=True, on_delete=models.CASCADE)
    descripcion_proy = models.ForeignKey(DescripcionProyecto, null=True, on_delete=models.CASCADE)
    suelo = models.ForeignKey(Suelo, null=True, on_delete=models.CASCADE)
    agua = models.ForeignKey(Agua, null=True, on_delete=models.CASCADE)
    aire = models.ForeignKey(Aire, null=True, on_delete=models.CASCADE)
    c_fisico = models.ForeignKey(ConclusionFisico, null=True, on_delete=models.CASCADE)
    forestal = models.ForeignKey(Forestal, null=True, on_delete=models.CASCADE)
    flora = models.ForeignKey(Flora, null=True, on_delete=models.CASCADE)
    fauna = models.ForeignKey(Fauna, null=True, on_delete=models.CASCADE)
    c_biologico = models.ForeignKey(ConclusionBiologico, null=True, on_delete=models.CASCADE)
    social = models.ForeignKey(Social, null=True, on_delete=models.CASCADE)
    economica = models.ForeignKey(Economica, null=True, on_delete=models.CASCADE)
    cultural = models.ForeignKey(Cultural, null=True, on_delete=models.CASCADE)
    c_cultural = models.ForeignKey(ConclusionCultural, null=True, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividades, null=True, on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentarios, null=True, on_delete=models.CASCADE)
    diagrama = models.ForeignKey(Diagrama, null=True, on_delete=models.CASCADE)
    talento = models.ForeignKey(TalentoHumano, null=True, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicios, null=True, on_delete=models.CASCADE)
    pasaje = models.ForeignKey(Pasajes, null=True, on_delete=models.CASCADE)
    recursos = models.ForeignKey(RecursosMateriales, null=True, on_delete=models.CASCADE)
    oficina = models.ForeignKey(Oficina, null=True, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumos, null=True, on_delete=models.CASCADE)
    plan = models.ForeignKey(PlanInversion, null=True, on_delete=models.CASCADE)
    informacion = models.ForeignKey(Informacion, null=True, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Responsable, null=True, on_delete=models.CASCADE)

