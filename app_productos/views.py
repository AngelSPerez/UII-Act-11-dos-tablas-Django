from django.shortcuts import render, get_object_or_404, redirect
# Importamos los modelos y formularios correctos
from .models import Productos, Categorias
# MODIFICADO: Importar CategoriaForm también
from .forms import ProductoForm, CategoriaForm

def listar_productos(request):
    """
    Vista para leer (Read) y listar todos los productos.
    """
    productos = Productos.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    """
    Vista para ver el detalle (Read) de un solo producto.
    """
    producto = get_object_or_404(Productos, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

def crear_producto(request):
    """
    Vista para Crear (Create) un nuevo producto.
    """
    if request.method == 'POST':
        # Pasamos request.FILES para manejar la subida de la imagen (foto_prod)
        form = ProductoForm(request.POST, request.FILES) # Corregido de ProductosForm
        if form.is_valid():
            form.save()
            # Corregido: redirigimos a la lista usando el nuevo nombre 'app_productos'
            return redirect('app_productos:listar_productos') 
    else:
        form = ProductoForm() # Corregido de ProductosForm
    return render(request, 'formulario_producto.html', {'form': form, 'titulo': 'Crear Producto'})

def editar_producto(request, producto_id):
    """
    Vista para Actualizar (Update) un producto existente.
    """
    producto = get_object_or_404(Productos, id=producto_id)
    if request.method == 'POST':
        # Pasamos 'instance=producto' para que el form sepa qué objeto editar
        # y 'request.FILES' por si se cambia la imagen
        form = ProductoForm(request.POST, request.FILES, instance=producto) # Corregido
        if form.is_valid():
            form.save()
            # Corregido: usamos 'app_productos'
            return redirect('app_productos:detalle_producto', producto_id=producto.id)
    else:
        # Precargamos el formulario con los datos del producto existente
        form = ProductoForm(instance=producto) # Corregido
    return render(request, 'formulario_producto.html', {'form': form, 'titulo': 'Editar Producto'})

def borrar_producto(request, producto_id):
    """
    Vista para Borrar (Delete) un producto.
    """
    producto = get_object_or_404(Productos, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        # Corregido: usamos 'app_productos'
        return redirect('app_productos:listar_productos')
    # Esta vista usualmente muestra una página de confirmación
    return render(request, 'confirmar_borrar.html', {'producto': producto})

# --- INICIO DE NUEVAS VISTAS PARA CATEGORÍAS ---

def listar_categorias(request):
    """
    Vista para leer (Read) y listar todas las categorías.
    """
    categorias = Categorias.objects.all()
    return render(request, 'listar_categorias.html', {'categorias': categorias})

def crear_categoria(request):
    """
    Vista para Crear (Create) una nueva categoría.
    """
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_productos:listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'formulario_categoria.html', {'form': form, 'titulo': 'Crear Categoría'})

def editar_categoria(request, categoria_id):
    """
    Vista para Actualizar (Update) una categoría existente.
    """
    categoria = get_object_or_404(Categorias, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('app_productos:listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'formulario_categoria.html', {'form': form, 'titulo': 'Editar Categoría'})

def borrar_categoria(request, categoria_id):
    """
    Vista para Borrar (Delete) una categoría.
    """
    categoria = get_object_or_404(Categorias, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('app_productos:listar_categorias')
    return render(request, 'confirmar_borrar_categoria.html', {'categoria': categoria})

# --- FIN DE NUEVAS VISTAS PARA CATEGORÍAS ---

# ... (todas tus vistas de productos y categorías van aquí arriba) ...

# --- VISTA PARA EL PANEL DE ADMINISTRACIÓN ---

def admin_tables(request):
    """
    Vista para mostrar el panel de administración de tablas.
    """
    return render(request, 'admin_tables.html')