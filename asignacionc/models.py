from django.db import models
from django.contrib import admin

class Alumno(models.Model):
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    correo = models.EmailField(max_length=70)
    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nom_materia = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=120)
    alumnos = models.ManyToManyField(Alumno, through='Grado')
    def __str__(self):
        return self.nom_materia

class Grado(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

class GradoInLine(admin.TabularInline):
    model = Grado
    extra = 1

class AlumnoAdmin(admin.ModelAdmin):
    inlines = (GradoInLine,)

class MateriaAdmin(admin.ModelAdmin):
    inlines = (GradoInLine,)


# Create your models here.
