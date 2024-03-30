from django.db import models

# Create your models here.

class Curso(models.Model):

    Nombre = models.CharField(max_length=40)
    Comision = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.Nombre}    Comision: {self.Comision}"
    

class Alumno(models.Model):

    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Documento = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.Nombre} Apellido: {self.Apellido} Documento: {self.Documento}"
    
class Profesor(models.Model):

    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Documento = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.Nombre} Apellido: {self.Apellido} Documento: {self.Documento}"