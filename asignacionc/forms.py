from django import forms
from .models import Materia, Alumno

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ('nom_materia', 'descripcion', 'alumnos')
    def __init__(self, *args, **kwargs):
        super(MateriaForm, self).__init__(*args, **kwargs)
        self.fields["alumnos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["alumnos"].help_text = "Ingrese los alumnos inscritos en materia"
        self.fields["alumnos"].queryset = Actor.objects.all()
