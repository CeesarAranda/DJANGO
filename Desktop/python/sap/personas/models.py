from django.db import models




class Domicilio(models.Model):
    calle = models.CharField(max_length= 200)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=200)

    def __str__(self):
        return f'Domicilio: {self.calle} n.{self.no_calle} {self.pais}'

# Con esto se crea una tabla con los campos especificados
class Persona(models.Model):
    objects = None
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    #llave foranea
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'Persona {self.id}:  {self.nombre} {self.apellido}'