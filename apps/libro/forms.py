from django import forms

from models import Libro,Autor

class LibroForm(forms.ModelForm):
    class Meta():
        model = Libro
        fields = [
            'portada',
            'titulo',
            'autores',
            'editor',
            'fecha_publicacion',
            
        ]
        labels = {
            'portada': 'Portada',
            'titulo': 'Titulo',
            'autores': 'Autores',
            'editor': 'Editor',
            'fecha_publicacion': 'Fecha de publicacion',
            

        }        
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control border-info'}),
            'autores': forms.CheckboxSelectMultiple(attrs={'class':'form-check-input border-info'}),
            'editor': forms.Select(attrs={'class':'form-select border-info'}),
            'fecha_publicacion': forms.TextInput(attrs={'class':'form-control border-info'}),
            
        }

class AutorForm(forms.ModelForm):
    class Meta():
        model = Autor
        fields = [
            'nombre',
            'apellido',
            'email',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Email',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control border-info'}),
            'apellido': forms.TextInput(attrs={'class':'form-control border-info'}),
            'email': forms.TextInput(attrs={'class':'form-control border-info'}),

        }