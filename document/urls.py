from django.urls import path
from . import views
from document.views import *

urlpatterns = [
    path('datos/', views.datos_proyecto, name='datos_proyecto'),
    path('documentos_intencion/', DocumentosIntencion.as_view(), name='documentos_intencion'),

]