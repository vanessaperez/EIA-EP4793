from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views.generic import TemplateView
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class HomePageView(TemplateView):
    template_name = 'home.html'


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            messages.success(request, 'Your account has been created!')
            form.save()
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