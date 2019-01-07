from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from django.forms import TextInput


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'doc_identidad')
        labels = {
            'first_name': _('Nombre'),
            'last_name': _('Apellido'),
            'email': _('Correo'),
            'doc_identidad': _('Cédula de Identidad')
        }
        widgets = {
            'doc_identidad': TextInput(attrs={'placeholder': 'V-12345678'}),
        }


class CustomUserChangeForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'doc_identidad')
        labels = {
            'first_name': _('Nombre'),
            'last_name': _('Apellido'),
            'email': _('Correo'),
            'doc_identidad': _('Documento Identidad')
        }


