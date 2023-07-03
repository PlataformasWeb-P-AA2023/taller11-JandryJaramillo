from django.db import models

class Edificio(models.Model):
    tipoE = (
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
        )
    
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, \
                            choices=tipoE)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    costo = models.CharField(max_length=100)
    numCuartos = models.DecimalField(max_digits=100, decimal_places=2)
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="edificioRN")

    def __str__(self):
        return "%s %s %s" % (self.nombre,
                self.costo,
                self.numCuartos)
