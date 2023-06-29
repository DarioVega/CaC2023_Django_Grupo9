from django import forms

def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise forms.ValidationError('El nombre no puede contener números. %(valor)s',
                                    code='invalid',
                                    params={'valor': value}) 

def validar_longitud_minima(value):
    if len(value) < 2:
        raise forms.ValidationError('El nombre del producto debe tener al menos 2 caracteres.')

class AgregarForm(forms.Form):
    nombre_producto = forms.CharField(
        # label='Nuevo Producto',
        max_length=50,
        validators=[solo_caracteres],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del producto',
            }
        )
    )

    def clean_nombre_producto(self):
        nombre_producto = self.cleaned_data['nombre_producto']
        validar_longitud_minima(nombre_producto)
        return nombre_producto

    def clean(self):
        cleaned_data = super().clean()
        nombre_producto = cleaned_data.get('nombre_producto')
        if nombre_producto:
            validar_longitud_minima(nombre_producto)
