from django.shortcuts import render
from .forms import *
from django.forms.formsets import formset_factory
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic import View
from django.template import RequestContext, Context
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

def datos_proyecto(request):
    SueloFormSet = formset_factory(SueloForm, extra=2, max_num=10)
    AguaFormSet = formset_factory(AguaForm, extra=2, max_num=10)

    if request.method == 'POST':
        form_proyecto = DatosProyectoForm(request.POST, prefix='proyecto')
        form_solicitante = SolicitanteForm(request.POST, prefix='solicitante')
        form_organizacion = OrganizacionForm(request.POST, prefix='organizacion')
        form_espacio = DatosEspacioForm(request.POST, prefix='espacio')
        form_personal = DatosPersonalForm(request.POST, prefix='personal')
        form_documento = DatosDocumentoForm(request.POST, prefix='documento')
        form_descripcion = DescripcionProyectoForm(request.POST, request.FILES, prefix='descripcion')
        form_suelo = SueloFormSet(request.POST, prefix='suelo')
        form_agua = AguaFormSet(request.POST, prefix='agua')


        arrayform = [
            form_proyecto, form_solicitante, form_organizacion, form_espacio, form_personal,
            form_documento, form_descripcion
        ]

        arrayformset = [
            form_suelo, form_agua
        ]

        for array in arrayform:
            if array.is_valid():
                proyecto = form_proyecto.save(commit=False)
                proyecto.titulo = form_proyecto.cleaned_data['titulo']
                proyecto.save()
                solicitante = form_solicitante.save(commit=False)
                solicitante.nombre = form_solicitante.cleaned_data['nombre']
                solicitante.save()
                organizacion = form_organizacion.save(commit=False)
                organizacion.nombre = form_organizacion.cleaned_data['nombre']
                organizacion.save()
                espacio = form_espacio.save(commit=False)
                espacio.tenencia_tierra = form_espacio.cleaned_data['tenencia_tierra']
                espacio.save()
                personal = form_personal.save(commit=False)
                personal.nombre_eia = form_personal.cleaned_data['nombre_eia']
                personal.save()
                documento = form_documento.save(commit=False)
                documento.ciudad = form_documento.cleaned_data['ciudad']
                documento.save()
                descripcion = form_descripcion.save(commit=False)
                descripcion.objetivo_general = form_descripcion.cleaned_data['objetivo_general']
                descripcion.save()


        for arrays in arrayformset:
            if arrays.is_valid():
                for document in arrays:
                    document.save()
                return redirect('documentos_intencion')
    else:
        form_proyecto = DatosProyectoForm(prefix='proyecto')
        form_solicitante = SolicitanteForm(prefix='solicitante')
        form_organizacion = OrganizacionForm(prefix='organizacion')
        form_espacio = DatosEspacioForm(prefix='espacio')
        form_personal = DatosPersonalForm(prefix='personal')
        form_documento = DatosDocumentoForm(prefix='documento')
        form_descripcion = DescripcionProyectoForm(prefix='descripcion')
        form_suelo = SueloFormSet(prefix='suelo')
        form_agua = AguaFormSet(prefix='agua')

    contexto = {'form_proyecto': form_proyecto,
                'form_solicitante': form_solicitante,
                'form_organizacion': form_organizacion,
                'form_espacio': form_espacio,
                'form_personal': form_personal,
                'form_documento': form_documento,
                'form_descripcion': form_descripcion,
                'form_suelo': form_suelo,
                'form_agua': form_agua,

               }

    return render(request, 'datos_proyecto/datos_proyecto.html', contexto)






#def documentos_intencion(request):
#
#    if request.method == 'GET':
#        # Para admins muestro todos los documentos de intencion
#        #if request.user.is_superuser:
#        documentos = DatosProyecto.objects.all()
#        # Para usuarios solicitantes, muestro solo SUS solicitudes
#        #else:
#        #    documentos = DatosProyecto.objects.get(solicitante__cedula=request.user.doc_identidad)

#        context = {}
#        context['documentos'] = documentos
#        return context

class DocumentosIntencion(TemplateView):
    template_name = 'datos_proyecto/documentos_intencion.html'

    def get_context_data(self, **kwargs):
        context = super(DocumentosIntencion, self).get_context_data(**kwargs)

        documentos = DatosProyecto.objects.all()
        
        context['documentos'] = documentos

        return context





