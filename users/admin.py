from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    '''
        Aqui se establece la conexion entre el modelo
        y la pagina admin de la aplicacion web
    '''
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Datos Personales', {'fields': ('first_name', 'last_name', 'doc_identidad')}),
        ('Permisología', {
            'fields': ('groups', 'user_permissions', 'is_superuser',
                       'is_staff', 'is_active')})
    )

admin.site.register(CustomUser, CustomUserAdmin)

