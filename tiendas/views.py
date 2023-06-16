from django.shortcuts import render

# Create your views here.
def tiendas(request):
    return render(request,'tiendas/tiendas.html')