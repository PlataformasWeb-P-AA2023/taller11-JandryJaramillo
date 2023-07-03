from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from condominios.models import *

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese direccion por favor'),
            'ciudad': _('Ingrese ciudad por favor'),
            'tipo': _('Seleccione tipo por favor'),
        }

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'costo', 'numCuartos', 'edificio']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'costo': _('Ingrese costo por favor'),
            'numCuartos': _('Ingrese número de cuartos por favor'),
            'edificio': _('Seleccione edificio por favor'),
        }