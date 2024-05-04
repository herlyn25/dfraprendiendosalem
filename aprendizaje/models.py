from django.db import models

# Create your models here.
class Numeros(models.Model):   
    familia = models.CharField(max_length=100)
    representacion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

class Letras(models.Model):
    descripcion = models.CharField(max_length=100)
    representacion = models.CharField(max_length=100)