from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto

admin.site.register(Categoria)
# admin.site.register(Producto) <---- ESTA ES LA FORMA DE ANTES DE HACERLO


@admin.register(Producto)  # <--------   ESTA ES LA NUEVA FORMA
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "precio",
        "categoria",
        "fecha_registro",
    )
    list_editable = (
        "precio",
        "categoria",
    )
