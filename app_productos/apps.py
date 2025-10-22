from django.apps import AppConfig

# CAMBIADO: El nombre de la clase debe ser AppProductosConfig
class AppProductosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_productos'