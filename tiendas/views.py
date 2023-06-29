from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from tiendas.forms import AgregarForm
from tiendas.models import Tienda

class TiendasView(View):
    template_name = 'tiendas/tiendas.html'

    def get(self, request):
        agregar_form = AgregarForm()
        tiendas = Tienda.objects.all().order_by('nombre')
        context = {
            'agregar_form': agregar_form,
            'tiendas': tiendas
        }
        return render(request, self.template_name, context)

    def post(self, request):
        if 'eliminar' in request.POST:
            tienda_id = int(request.POST.get('eliminar'))
            self.eliminar_tienda(request, tienda_id)
            messages.success(request, 'La tienda se ha eliminado correctamente')
            return redirect('tiendas')
        else:
            agregar_form = AgregarForm(request.POST)
            if agregar_form.is_valid():
                agregar_form.save()
                messages.success(request, 'La tienda se ha agregado correctamente')
                return redirect('tiendas')
            else:
                messages.error(request, 'Ha ocurrido un error en el formulario')
                agregar_form = AgregarForm()

        tiendas = Tienda.objects.all().order_by('nombre')

        context = {
            'agregar_form': agregar_form,
            'tiendas': tiendas
        }

        return render(request, self.template_name, context)

    def eliminar_tienda(self, request, tienda_id):
        tienda = Tienda.objects.get(id=tienda_id)
        tienda.delete()

class EliminarTiendaView(View):

    def post(self, request, tienda_id):
        tienda = Tienda.objects.get(id=tienda_id)
        tienda.delete()
        return redirect('tiendas')
