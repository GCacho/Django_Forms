from django.contrib import admin
from orders.models import Clientes, Articulos, Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):  # Para acomodar los datos en tabla al seleccionar Clientess en Admin Panel
    list_display=('nombre','direccion','email','tfno')
    search_fields=('nombre','email') # Para habilitar barra de busqueda por nombre y correo


class ArticulosAdmin(admin.ModelAdmin):
    list_display=('nombre','seccion','precio')
    list_filter=('seccion',) # Crea una tabla para poder filtrar los datos pos seccion


class PedidosAdmin(admin.ModelAdmin):
    list_display=('numero','fecha')
    list_filter=('fecha',) # Filtrar por fecha
    date_hierarchy='fecha'

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)