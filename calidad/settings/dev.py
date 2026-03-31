from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# 🔹 STATICFILES_DIRS (solo desarrollo) - “Busca archivos estáticos también en esta carpeta global”, busca archivos estáticos adicionales fuera de las apps
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_ROOT = BASE_DIR / 'media'

# Agrega esto si quieres servir media en desarrollo, aunque ya viene de base, esto lo deja explícito y claro
MEDIA_URL = '/media/'