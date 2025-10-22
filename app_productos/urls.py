from django.urls import path
from . import views

app_name = 'app_productos'

urlpatterns = [
    # --- RUTA PARA EL NUEVO PANEL DE ADMIN ---
    path('', views.admin_tables, name='admin_tables'),

    # --- Rutas de Productos ---
    path('productos/', views.listar_productos, name='listar_productos'),
    path('<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('borrar/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),

# --- Rutas de Categorías ---
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    
    # --- AÑADE ESTA LÍNEA ---
    path('categorias/<int:categoria_id>/', views.detalle_categoria, name='detalle_categoria'),
    # -------------------------
    
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/borrar/<int:categoria_id>/', views.borrar_categoria, name='borrar_categoria'),


 
]