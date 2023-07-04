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
    
    def get_cuartos(self):
        
        cuartos = 0

        for d in self.edificioRN.all(): 
            cuartos = cuartos + d.numCuartos
        return cuartos
    
    def get_costoT(self):
        
        costoT = 0.0

        for d in self.edificioRN.all(): 
            costoT = costoT + d.costo
        return costoT

class Departamento(models.Model):
    nombreP = models.CharField(max_length=100)
    costo = models.FloatField()
    numCuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="edificioRN")

    def __str__(self):
        return "Propietario: %s - Costo del departamento: %s - Número de Cuartos del departamento: %s" % (self.nombreP,
                self.costo,
                self.numCuartos)
