from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect

def datos_proyecto(request):

    if request.method == 'POST':
        form = DatosProyectoForm(request.POST)
        form1 = SolicitanteForm(request.POST)
        form2 = OrganizacionForm(request.POST)
        arrayform = [form, form1, form2]

        for array in arrayform:
            if array.is_valid():
                document = form.save(commit=False)
                document.titulo = form.cleaned_data['titulo']
                document.save()
                document1 = form1.save(commit=False)
                document1.nombre = form1.cleaned_data['nombre']
                document1.save()
                document2 = form2.save(commit=False)
                document2.nombre1 = form2.cleaned_data['nombre']
                document2.save()
                return redirect('user_views.profile')
    else:
        form = DatosProyectoForm()
        form1 = SolicitanteForm()
        form2 = OrganizacionForm()
    return render(request, 'datos_proyecto/datos_proyecto.html', {'form': form, 'form1': form1, 'form2': form2})




'''
def datos_proyecto(request):
    if request.method == "POST":
        form = DatosProyectoForm(request.POST)
        form1 = SolicitanteForm(request.POST)
        form2 = OrganizacionForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.titulo = form.cleaned_data['titulo']
            document.save()


        if form1.is_valid():
            document1 = form1.save(commit=False)
            document1.nombre = form1.cleaned_data['nombre']
            document1.save()


        if form2.is_valid():
            document2 = form2.save(commit=False)
            document2.nombre1 = form2.cleaned_data['nombre']
            document2.save()
            return redirect('user_views.profile')
    else:
        form = DatosProyectoForm()
        form1 = SolicitanteForm()
        form2 = OrganizacionForm()
    return render(request, 'datos_proyecto/datos_proyecto.html', {'form': form, 'form1': form1, 'form2':form2})

'''


'''
def datos_proyecto(request):
    if request.method == "POST":
        form = SolicitanteForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.nombre = form.cleaned_data['nombre']
            document.save()
            #return redirect('datos_organizacion')
    else:
        form = SolicitanteForm()
    return render(request, 'datos_proyecto/datos_proyecto.html', {'form': form})


def datos_solicitante(request):
    if request.method == "POST":
        form1 = SolicitanteForm(request.POST)
        if form1.is_valid():
            document = form1.save(commit=False)
            document.nombre = form1.cleaned_data['nombre']
            document.save()
            #return redirect('datos_organizacion')
    else:
        form1 = SolicitanteForm()
    return render(request, 'datos_proyecto/datos_proyecto.html', {'form': form1})

def datos_organizacion(request):
    if request.method == "POST":
        form2 = OrganizacionForm(request.POST)
        if form2.is_valid():
            document = form2.save(commit=False)
            document.nombre = form2.cleaned_data['nombre']
            document.save()
            #return redirect('login')
    else:
        form2 = OrganizacionForm()
    return render(request, 'datos_proyecto/datos_proyecto.html', {'form': form2})

'''