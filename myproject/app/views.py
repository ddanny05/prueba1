from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# Crear
def producto_crear(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_lista')
    else:
        form = ProductoForm()
    return render(request, 'app/producto_form.html', {'form': form})

# Leer
def producto_lista(request):
    productos = Producto.objects.all()
    return render(request, 'app/producto_lista.html', {'productos': productos})

# Actualizar
def producto_editar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_lista')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'app/producto_form.html', {'form': form})

# Eliminar
def producto_eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.delete()
        return redirect('producto_lista')
    return render(request, 'app/producto_confirm_delete.html', {'producto': producto})
