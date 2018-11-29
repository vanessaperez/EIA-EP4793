from django.db import models
from django import forms


class DatosProyecto(models.Model):
    titulo = models.CharField(max_length=130)
    ubicacion = models.CharField(max_length=130)
    area = models.CharField(max_length=130)
    tipo = models.CharField(max_length=130)
    status = models.CharField(max_length=20)
    solicitante = models.ForeignKey(DatosSolicitante, null=True)
    organizacion = models.ForeignKey(DatosOrganizacion, null=True)
    d_espacio = models.ForeignKey(DatosEspacio, null=True)
    d_personal = models.ForeignKey(DatosPersonal, null=True)
    d_documento = models.ForeignKey(DatosDocumento, null=True)
    descripcion_proy = models.ForeignKey(DescripcionProyecto, null=True)
    suelo = models.ForeignKey(Suelo, null=True)
    agua = models.ForeignKey(Agua, null=True)
    aire = models.ForeignKey(Aire, null=True)



class DatosSolicitante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.PositiveIntegerField()
    telefono = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class DatosOrganizacion(models.Model):

    RAZON_CHOICES = (
        ('pnatural', 'Natural'),
        ('pjuridica', 'Jurídica'),
    )

    natural = 'natural'

    nombre = models.CharField(max_length=60)
    razon_social = models.CharField(choices=RAZON_CHOICES, default=natural, max_length=100)
    print(razon_social)
    rif = models.CharField(max_length=30)
    dir_oficina = models.CharField(max_length=130)
    representante_legal = models.CharField(max_length=130)
    telefono = models.CharField(max_length=30)
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
    nombre_eia = models.CharField(max_length=30)
    apellido_eia = models.CharField(max_length=30)
    cedula_eia = models.PositiveIntegerField()
    nivel_eia = models.CharField(max_length=40)
    nombre_fisico = models.CharField(max_length=30)
    apellido_fisico = models.CharField(max_length=30)
    cedula_fisico = models.PositiveIntegerField()
    nivel_fisico = models.CharField(max_length=40)
    nombre_bio = models.CharField(max_length=30)
    apellido_bio = models.CharField(max_length=30)
    cedula_bio = models.PositiveIntegerField()
    nivel_bio = models.CharField(max_length=40)
    nombre_eco = models.CharField(max_length=30)
    apellido_eco = models.CharField(max_length=30)
    cedula_eco = models.PositiveIntegerField()
    nivel_eco = models.CharField(max_length=40)
    nombre_desa = models.CharField(max_length=30)
    apellido_desa = models.CharField(max_length=30)
    cedula_desa = models.PositiveIntegerField()
    nivel_desa = models.CharField(max_length=40)

class DatosDocumento(models.Model):
    fecha = models.DateField()
    ciudad = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)

class DescripcionProyecto(models.Model):
    objetivo_general = models.TextField(max_length=300)
    objetivo_especifico = models.TextField(max_length=1000)
    justificacion = models.TextField(max_length=1000)
    imagen = models.ImageField(upload_to="static/img", null=True)
    marco = models.TextField(max_length=2000)

class Suelo(models.Model):
    caracteristicas = models.CharField(max_length=100)
    tipo_atributo = models.CharField(max_length=100)
    tipo_comentario = models.CharField(max_length=100)
    homo_atributo = models.CharField(max_length=100)
    homo_comentario = models.CharField(max_length=100)
    textura_atributo = models.CharField(max_length=100)
    textura_comentario = models.CharField(max_length=100)


class Agua(models.Model):
    caracteristicas = models.CharField(max_length=100)
    recurso_atributo = models.CharField(max_length=100)
    recurso_comentario = models.CharField(max_length=100)
    drenaje_atributo = models.CharField(max_length=100)
    drenaje_comentario = models.CharField(max_length=100)
    corriente_atributo = models.CharField(max_length=100)
    corriente_comentario = models.CharField(max_length=100)

class Aire(models.Model):

    caracteristicas = models.CharField(max_length=100)
    clima_atributo = models.CharField(max_length=100)
    clima_comentario = models.CharField(max_length=100)
    temp_atributo = models.CharField(max_length=100)
    temp_comentario = models.CharField(max_length=100)
    vientos_atributo = models.CharField(max_length=100)
    vientos_comentario = models.CharField(max_length=100)