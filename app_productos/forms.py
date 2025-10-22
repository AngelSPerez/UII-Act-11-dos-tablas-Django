from django import forms
from .models import Productos, Categorias


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['nombre', 'descripcion']

# Formulario para el modelo Producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            'nombre', 
            'descripcion', 
            'precio_venta', 
            'stock',
            'foto_prod', 
            'categoria'
        ]