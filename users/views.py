from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class HomePageView(TemplateView):
    template_name = 'home.html'

class LoginView(TemplateView):
	template_name = 'registration/login.html'


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            messages.success(request, 'Your account has been created!')
            form.save()

            # Envio correo al nuevo usuario
            email_subject = "¡Bienvenido a EIA!"
            to = [user.username]
            bcc = ['11-10968@usb.ve']
            ctx = {
                'first_name': user.first_name.encode('utf-8'),
                'last_name': user.last_name.encode('utf-8'),
                'doc_identidad': user.doc_identidad,
            }
            message = '''
Nombre: {first_name}\n
Apellido: {last_name}\n
Documento de identidad: {doc_identidad}\n
            '''.format(**ctx)
            msg = EmailMessage(email_subject, message, to=to, bcc=bcc)
            msg.send()
            # ANADIR EL BACKEND DEL CORREO ACA, CREAR ALGO EN HEROKU PARA ESO

            # Redirect al login
            return redirect('login')

    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html')




class NewUser(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    ''' Class based view encargada de la creacion de un nuevo usuario'''
    model = CustomUser
    template_name = 'signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('new_user')
    permission_required = 'users.add_customuser'

class UpdateUser(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    ''' Class based view encargada de la edicion de un usuario'''
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'usuario_update_form.html'
    success_url = reverse_lazy('new_user')
    permission_required = 'users.change_customuser'
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial']['rol'] = self.object.groups.all().first().pk
        return kwargs

class DeleteUser(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    ''' Class based view encargada de la eliminacion de un usuario'''
    template_name = 'user_confirm_delete.html'
    model = CustomUser
    success_url = reverse_lazy('users_list')
    permission_required = 'users.delete_customuser'

class UserList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    ''' Class based view encargada de listar todos los usuarios de la tabla Usuario'''
    template_name = 'usuario_list.html'
    model = CustomUser
    permission_required = 'users.view_customuser'


