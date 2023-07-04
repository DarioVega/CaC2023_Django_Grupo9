from django.contrib import admin
from productos.models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_editable = ()
    list_display_links = ()
    search_fields = ['nombre']

admin.site.register(Producto, ProductoAdmin)
