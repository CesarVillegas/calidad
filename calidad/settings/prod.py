from .base import *
import os
from pathlib import Path

DEBUG = False
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1').split(',')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
        'CONN_MAX_AGE': 60,
    }
}


# STATIC_ROOT Es donde Django reúne todos los static con collectstatic al desplegar en producción. ❌ No se usa en desarrollo
STATIC_ROOT = '/var/www/userena.cl_calidad/static'

# Media 👉 Carpeta real donde se guardan archivos subidos
MEDIA_ROOT = '/var/www/userena.cl_calidad/media'

# Esto no es necesario en producción si usas collectstatic, pero lo dejo comentado para que quede claro que no se usa en producción, solo en desarrollo
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]


# Seguridad
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True 🔴 2. Falta HTTPS enforcement (muy recomendado) CICULS con balanceador llega solo puerto 80 al servidor

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
# X_FRAME_OPTIONS = 'DENY'
