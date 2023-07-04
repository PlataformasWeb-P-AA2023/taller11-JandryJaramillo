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

    def clean_ciudad(self):
        ciudad = self.cleaned_data.get('ciudad')
        if ciudad[0].upper() == 'L':
            raise forms.ValidationError(
                "El nombre de la ciudad no puede iniciar con la letra mayúscula L")
        return ciudad

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombreP', 'costo', 'numCuartos', 'edificio']
        labels = {
            'nombreP': _('Ingrese nombre completo del dueño'),
            'costo': _('Ingrese costo por favor'),
            'numCuartos': _('Ingrese número de cuartos por favor'),
            'edificio': _('Seleccione edificio por favor'),
        }

    def clean_costo(self):
        costo = self.cleaned_data.get('costo')
        if costo > 100000:
            raise forms.ValidationError(
                "Costo de un departamento no puede ser mayor a $100 mil.")
        return costo

    def clean_numCuartos(self):
        numCuartos = self.cleaned_data.get('numCuartos')
        if numCuartos == 0 or numCuartos > 7:
            raise forms.ValidationError(
                "Número de cuartos no puede ser 0, ni mayor a 7")
        return numCuartos

    def clean_nombreP(self):
        nombreP = self.cleaned_data.get('nombreP')
        if len(nombreP.split()) < 3:
            raise forms.ValidationError(
                "El nombre completo de un propietario no debe tener menos de 3 palabras.")
        return nombreP

#class DepartamentoEditForm(ModelForm):

#    def __init__(self, departamento, *args, **kwargs):
        super(DepartamentoEditForm, self).__init__(*args, **kwargs)
        self.initial['departamento'] = departamento
        self.fields["departamento"].widget = forms.widgets.HiddenInput()
        print(departamento)

#    class Meta:
        model = Departamento
        fields = ['nombreP', 'costo', 'numCuartos', 'edificio']
        labels = {
            'nombreP': _('Ingrese nombre completo del dueño'),
            'costo': _('Ingrese costo por favor'),
            'numCuartos': _('Ingrese número de cuartos por favor'),
            'edificio': _('Seleccione edificio por favor'),
        }