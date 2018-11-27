from django.db import models
from django import forms


RAZON_CHOICES = [
   ('pnatural', 'Natural'),
   ('pjuridica', 'Juridica'),
]

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
    nombre = models.CharField(max_length=60)
    razon_social = forms.ChoiceField(choices=RAZON_CHOICES, widget=forms.RadioSelect())
    rif = models.CharField(max_length=30)
    dir_oficina = models.CharField(max_length=130)
    representante_legal = models.CharField(max_length=130)
    telefono = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

#class DatosEspacio(models.Model):

