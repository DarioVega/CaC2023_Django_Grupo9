from django import forms

def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise forms.ValidationError('El nombre no puede contener números. %(valor)s',
                                    code='invalid',
                                    params={'valor': value}) 

def validar_longitud_minima(value):
    if len(value) < 2:
        raise forms.ValidationError('El nombre del producto debe tener al menos 2 caracteres.')

class TiendasForm(forms.Form):
    nombre_tiendas = forms.CharField(
        label='Nueva Tienda',
        max_length=50,
        validators=[solo_caracteres],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre de la tienda',
            }
        )
    )

    def clean_nombre_tiendas(self):
        nombre_tiendas = self.cleaned_data['nombre_tiendas']
        validar_longitud_minima(nombre_tiendas)
        return nombre_tiendas

    def clean(self):
        cleaned_data = super().clean()
        nombre_tiendas = cleaned_data.get('nombre_tiendas')
        if nombre_tiendas:
            validar_longitud_minima(nombre_tiendas)
