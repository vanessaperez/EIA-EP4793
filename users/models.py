from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    doc_identidad = models.PositiveIntegerField()
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'doc_identidad']

    def __str__(self):
        return self.email
