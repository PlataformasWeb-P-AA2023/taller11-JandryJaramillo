from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('crear/edificio', views.crearEdificio, 
            name='crearEdificio'),
        path('editarEdificio/<int:id>', views.editarEdificio, 
            name='editarEdificio'),
        path('eliminar/edificio/<int:id>', views.eliminarEdificio, 
            name='eliminarEdificio'),
        # depatamentos
        path('crear/departamento/<int:id>', views.crearDepartamento, 
            name='crearDepartamento'),
        path('editar/departamento/<int:id>', views.editarDepartamento, 
            name='editarDepartamento'),
        path('eliminar/departamento/<int:id>', views.eliminarDepartamento, 
            name='eliminarDepartamento'),
 ]
