from django import forms
from tiendas.models import Tienda

def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise forms.ValidationError('El nombre no puede contener números. %(valor)s',
                                    code='invalid',
                                    params={'valor': value}) 

def validar_longitud_minima(value):
    if len(value) < 2:
        raise forms.ValidationError('El nombre del tienda debe tener al menos 2 caracteres.')

class AgregarForm(forms.Form):
    nombre_tienda = forms.CharField(
        max_length=50,
        validators=[solo_caracteres],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el tienda',
            }
        )
    )

    def clean_nombre_tienda(self):
        nombre_tienda = self.cleaned_data['nombre_tienda']
        validar_longitud_minima(nombre_tienda)
        return nombre_tienda

    def clean(self):
        cleaned_data = super().clean()
        nombre_tienda = cleaned_data.get('nombre_tienda')
        if nombre_tienda:
            validar_longitud_minima(nombre_tienda)

    def save(self):
        nombre = self.cleaned_data['nombre_tienda']
        tienda = Tienda(nombre=nombre)
        tienda.save()
