from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    #objects = CustomUserManager()

    first_name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    doc_identidad = models.CharField(max_length=10,
                                     validators=[RegexValidator(r'^[VEJPG]-\d+$',
                                                                'Formato de documento de identidad'
                                                                ' inválido. Los números deben '
                                                                'estar precedidos por V- o E-.'
                                                                )],
                                     verbose_name='Documento de Identidad',
                                     unique=True)
    email = models.EmailField('Dirección de correo electrónico', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'doc_identidad']

    @property
    def rol(self):
        """ Obtiene el rol del usuario """
        return self.groups.all().first()

    def __str__(self):
        return self.email

    def full_name(self):
        """ Retorna el nombre completo del usuario """
        return '{} {}'.format(self.first_name, self.last_name)

