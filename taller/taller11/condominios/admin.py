from django.contrib import admin

from condominios.models import *

class EdificioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'tipo')

admin.site.register(Edificio, EdificioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'costo', 'numCuartos', 'edificio')
    search_fields = ('nombre', 'costo')

admin.site.register(Departamento, DepartamentoAdmin)
