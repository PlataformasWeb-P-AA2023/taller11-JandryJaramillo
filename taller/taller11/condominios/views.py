from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext

from condominios.models import *

from condominios.forms import *

def index(request):

    edificios = Edificio.objects.all()
    
    informacion_template = {'edificios': edificios}
    
    return render(request, 'index.html', informacion_template)

def crearEdificio(request):
    
    if request.method=='POST':
        formulario = EdificioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearEdificio.html', diccionario)

def editarEdificio(request, id):
    
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm(instance=edificio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarEdificio.html', diccionario)

def eliminarEdificio(request, id):
    
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)

def crearDepartamento(request, id):
    
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm(instance=edificio)
    diccionario = {'formulario': formulario, 'edificio': edificio}

    return render(request, 'crearDepartamento.html', diccionario)

def editarDepartamento(request, id):
    
    departamento = Departamento.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST, instance=departamento)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm(instance=departamento)
    diccionario = {'formulario': formulario}

    return render(request, 'editarDepartamento.html', diccionario)

def eliminarDepartamento(request, id):
    
    departamento = Departamento.objects.get(pk=id)
    departamento.delete()
    return redirect(index)