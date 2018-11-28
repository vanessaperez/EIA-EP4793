from django.db import models
from django import forms


class DatosProyecto(models.Model):
    titulo = models.CharField(max_length=130)
    ubicacion = models.CharField(max_length=130)
    area = models.CharField(max_length=130)
    tipo = models.CharField(max_length=130)


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

class DatosLindero(models.Model):

    lindero_norte = models.CharField(max_length=100)
    lindero_sur = models.CharField(max_length=100)
    lindero_este = models.CharField(max_length=100)
    lindero_oeste = models.CharField(max_length=100)

class DatosCoordenadas(models.Model):
    coor_norte = models.CharField(max_length=100)
    coor_sur = models.CharField(max_length=100)
    coor_este = models.CharField(max_length=100)
    coor_oeste = models.CharField(max_length=100)