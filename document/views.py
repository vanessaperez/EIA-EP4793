from django.shortcuts import render
from .forms import *
from django.forms.formsets import formset_factory
from django.shortcuts import redirect
from django.contrib.auth.models import User

def datos_proyecto(request):

    #MediofisicoFormset = formset_factory(MedioFisicoForm, extra=2)
    if request.method == 'POST':
        form = DatosProyectoForm(request.POST)
        form1 = SolicitanteForm(request.POST)
        form2 = OrganizacionForm(request.POST)
        form3 = DatosEspacioForm(request.POST)
        form4 = DatosPersonal(request.POST)
        form5 = DatosDocumento(request.POST)
        form6 = DescripcionProyecto(request.POST, request.FILES)
        form7 = Suelo(request.POST)
        form8 = Agua(request.POST)
        form9 = Aire(request.POST)
        #formset = MediofisicoFormset(request.POST)

        arrayform = [
            form, form1, form2, form3, form4,
            form5, form6, form7, form8, form9
        ]

        for array in arrayform:
            if array.is_valid():
                document = form.save(commit=False)
                document.titulo = form.cleaned_data['titulo']
                document.save()
                document1 = form1.save(commit=False)
                document1.nombre = form1.cleaned_data['nombre']
                document1.save()
                document2 = form2.save(commit=False)
                document2.nombre = form2.cleaned_data['nombre']
                document2.save()
                document3 = form3.save(commit=False)
                document3.tenencia_tierra = form3.cleaned_data['tenencia_tierra']
                document3.save()
                document4 = form4.save(commit=False)
                document4.nombre_eia = form4.cleaned_data['nombre_eia']
                document4.save()
                document5 = form5.save(commit=False)
                document5.ciudad = form5.cleaned_data['ciudad']
                document5.save()
                document6 = form6.save(commit=False)
                document6.objetivo_general = form6.cleaned_data['objetivo_general']
                document6.save()
                form7.save()
                form8.save()
                form9.save()
                #formset.save()
                #return redirect('users/profile/')
    else:
        form = DatosProyectoForm()
        form1 = SolicitanteForm()
        form2 = OrganizacionForm()
        form3 = DatosEspacioForm()
        form4 = DatosPersonalForm()
        form5 = DatosDocumentoForm()
        form6 = DescripcionProyectoForm()
        form7 = SueloForm()
        form8 = AguaForm()
        form9 = AireForm()
        #formset = MediofisicoFormset()
    return render(request, 'datos_proyecto/datos_proyecto.html',
                  {'form': form,
                   'form1': form1,
                   'form2': form2,
                   'form3': form3,
                   'form4': form4,
                   'form5': form5,
                   'form6': form6,
                   'form7': form7,
                   'form8': form8,
                   'form9': form9
                   })




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

def documentos_intencion(request):

    if request.method == 'GET':
        # Para admins muestro todos los documentos de intencion
        if request.user.is_superuser:
            documentos = DatosProyecto.objects.all()
        # Para usuarios solicitantes, muestro solo SUS solicitudes
        else:
            documentos = DatosProyecto.objects.get(solicitante__cedula=request.user.doc_identidad)

        context = {}
        context['documentos'] = documentos
        return context
