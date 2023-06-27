from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from django.contrib import messages

from productos.forms import AgregarForm

def productos(request):
    if request.method == 'POST':
        agregar_form = AgregarForm(request.POST)
        if agregar_form.is_valid():
            messages.success(request, 'Hemos recibido tus datos')
        else:
            agregar_form.add_error(None, 'Ha ocurrido un error en el formulario')  # Agregar mensaje de error al formulario
    elif request.method == 'GET':
        agregar_form = AgregarForm()
    else:
        return HttpResponseNotAllowed(f'Método {request.method} no soportado')

    context = {
        'agregar_form': agregar_form
    }

    return render(request, 'productos/productos.html', context)
