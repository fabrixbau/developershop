from django.shortcuts import render, get_object_or_404

from .models import Categoria, Producto

# Create your views here.
""" VISTAS PARA EL CATALOGO DE PRODUCTOS """


def index(request):
    listaProductos = Producto.objects.all()
    listaCategorias = Categoria.objects.all()

    # print(listaProductos)

    context = {"productos": listaProductos, "categorias": listaCategorias}
    return render(request, "index.html", context)


def productosPorCategoria(request, categoria_id):
    """VISTA PARA FILTRAR PRODUCTOS POR CATEGIORIA"""
    objCategoria = Categoria.objects.get(pk=categoria_id)
    listaProductos = objCategoria.producto_set.all()

    listaCategorias = Categoria.objects.all()

    context = {"categorias": listaCategorias, "productos": listaProductos}

    return render(request, "index.html", context)


def productosPorNombre(request):
    """vistas para filtrado de productos por nombre"""
    nombre = request.POST["nombre"]

    listaProductos = Producto.objects.filter(nombre__icontains=nombre)
    listaCategorias = Categoria.objects.all()

    context = {"productos": listaProductos, "categorias": listaCategorias}
    return render(request, "index.html", context)


def productoDetalle(request, producto_id):
    """Vistas para producto y su detalle"""
    # objProducto = Producto.objects.get(pk=producto_id)
    objProducto = get_object_or_404(Producto, pk=producto_id)
    context = {"producto": objProducto}

    return render(request, "producto.html", context)
