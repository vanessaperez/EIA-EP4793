from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator
import re


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    doc_identidad = models.CharField(max_length=10,
                                     validators=[RegexValidator(re.compile('/^[V|E|J|P]-[0-9]{5,9}$/'),
                                                                'Formato de documento de identidad'
                                                                ' inválido. Los números deben '
                                                                'estar precedidos por V- o E-.'
                                                                )],
                                     verbose_name='Documento de Identidad',
                                     unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'doc_identidad']

    def __str__(self):
        return self.email


