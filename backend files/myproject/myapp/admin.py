from django.contrib import admin
from django.urls import path, include
from .models import *

admin.site.register(Usuario)
admin.site.register(Turno)
admin.site.register(HistoralDeCitas)
admin.site.register(Profesional)
admin.site.register(Mensajes)
admin.site.register(Pago)
admin.site.register(Valoracion)
