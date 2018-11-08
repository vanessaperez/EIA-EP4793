from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect

def datos_proyecto(request):
    if request.method == "POST":
        form = DatosProyectoForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.titulo = form.cleaned_data['titulo']
            document.save()
            return redirect('datos_solicitante')
    else:
        form = DatosProyectoForm()
    return render(request, 'datos_proyecto/datos_proyecto.html', {'form': form})

def datos_solicitante(request):
    if request.method == "POST":
        form = SolicitanteForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.nombre = form.cleaned_data['nombre']
            document.save()
            return redirect('datos_organizacion')
    else:
        form = SolicitanteForm()
    return render(request, 'datos_proyecto/datos_solicitante.html', {'form': form})

def datos_organizacion(request):
    if request.method == "POST":
        form = OrganizacionForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.nombre = form.cleaned_data['nombre']
            document.save()
            return redirect('login')
    else:
        form = OrganizacionForm()
    return render(request, 'datos_proyecto/datos_organizacion.html', {'form': form})