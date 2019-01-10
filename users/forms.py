from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from django.forms import TextInput
from django.contrib.auth.models import Group


class CustomUserCreationForm(UserCreationForm):
    '''
        Aqui se implementa el formulario para la creacion
        de nuevos usuarios del sistema
    '''
    rol = forms.ModelChoiceField(queryset=Group.objects.all(), label='Rol')
    class Meta(UserCreationForm.Meta):
        '''
            Aqui se especifica que datos se tienen que incluir en
            el formulario
        '''
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'doc_identidad', 'username')

    def save(self, commit=True):
        instance = super().save(commit)
        rol = self.cleaned_data['rol']
        instance.groups.set([rol])
        return instance

class CustomUserChangeForm(UserChangeForm):
    '''
        Clase que implementa el formulario para la actualizacion
        de los datos de un usuario que ya existe en el sistema
    '''
    rol = forms.ModelChoiceField(queryset=Group.objects.all(), label='Rol')
    class Meta(UserChangeForm.Meta):
        '''
            Aqui se especifica que datos son los que se pueden modificar
        '''
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'doc_identidad')

    def save(self, commit=True):
        instance = super().save(commit)
        rol = self.cleaned_data['rol']
        instance.groups.set([rol])
        return instance
