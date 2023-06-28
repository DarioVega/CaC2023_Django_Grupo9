from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from django.contrib import messages

from tiendas.forms import TiendasForm

def tiendas(request):
    if request.method == 'POST':
        tiendas_form = TiendasForm(request.POST)
        if tiendas_form.is_valid():
            messages.success(request, 'Hemos recibido tus datos')
        else:
            tiendas_form.add_error(None, 'Ha ocurrido un error en el formulario')  # Agregar mensaje de error al formulario
    elif request.method == 'GET':
        tiendas_form = TiendasForm()
    else:
        return HttpResponseNotAllowed(f'Método {request.method} no soportado')

    context = {
        'tiendas_form': tiendas_form
    }

    return render(request, 'tiendas/tiendas.html', context)
