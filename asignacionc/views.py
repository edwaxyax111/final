from django.shortcuts import render
from django.contrib import messages
from .forms import MateriaForm
from asignacionc.models import Materia, Grado, Alumno

def materia_nueva(request):
    if request.method == "POST":
        formulario = MateriaForm(request.POST)
        if formulario.is_valid():
            materia = Materia.objects.create(nom_materia=formulario.cleaned_data['nom_materia'], descripcion = formulario.cleaned_data['descripcion'])
            for alumno_id in request.POST.getlist('alumnos'):
                grado = Grado(alumno_id=alumno_id, materia_id = materia.id)
                grado.save()
                messages.add_message(request, messages.SUCCESS, 'Materia Guardada Exitosamente')
        else:
            formulario = MateriaForm()
        return render(request, 'materias/materia_editar.html', {'formulario': formulario})



# Create your views here.
