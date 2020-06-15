from django.contrib import admin

# Register your models here.

from .models import Autores, Categorias, Clientes, Libros, LibrosPorAutor, PedidosCliente

admin.site.register(Autores)
admin.site.register(Categorias)
admin.site.register(Clientes)
admin.site.register(Libros)
admin.site.register(LibrosPorAutor)
admin.site.register(PedidosCliente)