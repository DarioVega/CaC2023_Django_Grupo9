from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AgregarForm
from .models import Producto, Tienda



def productos(request):
    if request.method == 'POST':
        if 'eliminar' in request.POST:
            producto_id = int(request.POST.get('eliminar'))
            eliminar_producto(request, producto_id)
            messages.success(request, 'El producto se ha eliminado correctamente')
            return redirect('productos')
        else:
            agregar_form = AgregarForm(request.POST)
            if agregar_form.is_valid():
                agregar_form.save()
                messages.success(request, 'El producto se ha agregado correctamente')
                return redirect('productos')
            else:
                messages.error(request, 'Ha ocurrido un error en el formulario')
    else:
        agregar_form = AgregarForm()
        
    productos = Producto.objects.all().order_by('nombre')
    tiendas = Tienda.objects.all().order_by('nombre')

    context = {
        'agregar_form': agregar_form,
        'productos': productos,
        'tiendas': tiendas
    }

    return render(request, 'productos/productos.html', context)

   

def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return redirect('productos')
