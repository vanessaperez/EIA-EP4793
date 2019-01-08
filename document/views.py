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
    AireFormSet = formset_factory(AireForm, extra=2, max_num=10)
    ForestalFormSet = formset_factory(ForestalForm, extra=2, max_num=10)
    FloraFormSet = formset_factory(FloraForm, extra=2, max_num=10)
    FaunaFormSet = formset_factory(FaunaForm, extra=2, max_num=10)
    SocialFormSet = formset_factory(SocialForm, extra=2, max_num=10)
    EcoFormSet = formset_factory(EconomicaForm, extra=2, max_num=10)
    CulturalFormSet = formset_factory(CulturalForm, extra=2, max_num=10)
    ActividadFormSet = formset_factory(ActividadesForm, extra=5, max_num=10)
    TalentoFormSet = formset_factory(TalentoHumanoForm, extra=2, max_num=10)
    ServicioFormSet = formset_factory(ServiciosForm, extra=2, max_num=10)
    PasajeFormSet = formset_factory(PasajesForm, extra=2, max_num=10)
    RecursosFormSet = formset_factory(RecursosMaterialesForm, extra=2, max_num=10)
    OficinaFormSet = formset_factory(OficinaForm, extra=2, max_num=10)
    InsumosFormSet = formset_factory(InsumosForm, extra=2, max_num=10)
    PlanFormSet = formset_factory(PlanInversionForm, extra=3, max_num=10)

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
        form_aire = AireFormSet(request.POST, prefix='aire')
        form_fisico = ConclusionFisicoForm(request.POST, prefix='fisico')
        form_forestal = ForestalFormSet(request.POST, prefix='forestal')
        form_flora = FloraFormSet(request.POST, prefix='flora')
        form_fauna = FaunaFormSet(request.POST, prefix='fauna')
        form_bio = ConclusionBiologicoForm(request.POST, prefix='biologico')
        form_social = SocialFormSet(request.POST, prefix='social')
        form_economica = EcoFormSet(request.POST, prefix='economica')
        form_cultural = CulturalFormSet(request.POST, prefix='cultural')
        form_sociocultural = ConclusionCulturalForm(request.POST, prefix='sociocultural')
        form_actividad = ActividadFormSet(request.POST, prefix='actividad')
        form_comentarios = ComentariosForm(request.POST, prefix='comentario')
        form_diagrama = DiagramaForm(request.POST, request.FILES, prefix='diagrama')
        form_talento = TalentoFormSet(request.POST, prefix='talento')
        form_servicio = ServicioFormSet(request.POST, prefix='servicio')
        form_pasaje = PasajeFormSet(request.POST, prefix='pasaje')
        form_recursos = RecursosFormSet(request.POST, prefix='recursos')
        form_oficina = OficinaFormSet(request.POST, prefix='oficina')
        form_insumos = InsumosFormSet(request.POST, prefix='insumos')
        form_plan = PlanFormSet(request.POST, prefix='plan')
        form_informacion = InformacionForm(request.POST, prefix='informacion')
        form_responsable = ResponsableForm(request.POST, prefix='responsable')



        arrayform = [
             form_proyecto, form_solicitante, form_organizacion, form_espacio,
             form_personal, form_documento, form_descripcion
        ]

        arrayformset = [form_suelo, form_agua, form_aire]

        bioformset = [form_forestal, form_flora, form_fauna]

        socialformset = [form_social, form_economica, form_cultural]

        inversionformset = [
            form_talento, form_servicio, form_pasaje, form_recursos, form_oficina,
            form_insumos, form_plan]

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

        if form_fisico.is_valid():
            form_fisico.save()

        for bio in bioformset:
            if bio.is_valid():
                for bios in bio:
                    bios.save()

        if form_bio.is_valid():
            form_bio.save()

        for social in socialformset:
            if social.is_valid():
                for sociales in social:
                    sociales.save()

        if form_sociocultural.is_valid():
            form_sociocultural.save()

        if form_actividad.is_valid():
            for activity in form_actividad:
                activity.save()

        if form_comentarios.is_valid():
            form_comentarios.save()

        if form_diagrama.is_valid():
            form_diagrama.save()

        for inversion in inversionformset:
            if inversion.is_valid():
                for talento in inversion:
                    talento.save()

        if form_informacion.is_valid() and form_responsable.is_valid():
            form_informacion.save()
            form_responsable.save()
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
        form_aire = AireFormSet(prefix='aire')
        form_fisico = ConclusionFisicoForm(prefix='fisico')
        form_forestal = ForestalFormSet(prefix='forestal')
        form_flora = FloraFormSet(prefix='flora')
        form_fauna = FaunaFormSet(prefix='fauna')
        form_bio = ConclusionBiologicoForm(prefix='biologico')
        form_social = SocialFormSet(prefix='social')
        form_economica = EcoFormSet(prefix='economica')
        form_cultural = CulturalFormSet(prefix='cultural')
        form_sociocultural = ConclusionCulturalForm(prefix='sociocultural')
        form_actividad = ActividadFormSet(prefix='actividad')
        form_comentarios = ComentariosForm(prefix='comentario')
        form_diagrama = DiagramaForm(prefix='diagrama')
        form_talento = TalentoFormSet(prefix='talento')
        form_servicio = ServicioFormSet(prefix='servicio')
        form_pasaje = PasajeFormSet(prefix='pasaje')
        form_recursos = RecursosFormSet(prefix='recursos')
        form_oficina = OficinaFormSet(prefix='oficina')
        form_insumos = InsumosFormSet(prefix='insumos')
        form_plan = PlanFormSet(prefix='plan')
        form_informacion = InformacionForm(prefix='informacion')
        form_responsable = ResponsableForm(prefix='responsable')

    contexto = {'form_proyecto': form_proyecto,
                'form_solicitante': form_solicitante,
                'form_organizacion': form_organizacion,
                'form_espacio': form_espacio,
                'form_personal': form_personal,
                'form_documento': form_documento,
                'form_descripcion': form_descripcion,
                'form_suelo': form_suelo,
                'form_agua': form_agua,
                'form_aire': form_aire,
                'form_fisico': form_fisico,
                'form_forestal': form_forestal,
                'form_flora': form_flora,
                'form_fauna': form_fauna,
                'form_bio': form_bio,
                'form_social': form_social,
                'form_economica': form_economica,
                'form_cultural': form_cultural,
                'form_sociocultural': form_sociocultural,
                'form_actividad': form_actividad,
                'form_comentarios': form_comentarios,
                'form_diagrama': form_diagrama,
                'form_talento': form_talento,
                'form_servicio': form_servicio,
                'form_pasaje': form_pasaje,
                'form_recursos': form_recursos,
                'form_oficina': form_oficina,
                'form_insumos': form_insumos,
                'form_plan': form_plan,
                'form_informacion': form_informacion,
                'form_responsable': form_responsable,

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





