from django import forms

from models import Editor

class EditorForm(forms.ModelForm):
    class Meta():
        model = Editor

        fields = [
            'nombre',
            'domicilio',
            'ciudad',
            'estado',
            'pais',
            'website',

        ]
        labels = {
            'nombre': 'Nombre',
            'domicilio': 'Domicilio',
            'ciudad': 'Ciudad',
            'estado': 'Estado',
            'pais': 'Pais',
            'website': 'Sitio Web',


        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control border-info'}),
            'domicilio': forms.Textarea(attrs={'class':'form-control border-info'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control border-info'}),
            'estado': forms.TextInput(attrs={'class':'form-control border-info'}),
            'pais': forms.TextInput(attrs={'class':'form-control border-info' }),
            'website': forms.TextInput(attrs={'class':'form-control border-info'}),

        }