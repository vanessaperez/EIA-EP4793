from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings


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


def edit_user(request, usuario):
    user = CustomUser.objects.get(pk=usuario)
    if request.method == 'POST':
        u_form = CustomUserChangeForm(request.POST, instance=user)
        if u_form.is_valid():
            user = u_form.save(commit=False)
            user.username = u_form.cleaned_data['email']
            u_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = CustomUserChangeForm(instance=user)
    return render(request, 'edit_user.html', {'u_form': u_form})