from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1').split(',')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  # o postgresql
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST'),
#         'PORT': os.getenv('DB_PORT'),
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/www/userena.cl_calidad/db.sqlite3',
    }
}

# STATIC_ROOT Es donde Django reúne todos los static con collectstatic al desplegar en producción. ❌ No se usa en desarrollo
STATIC_ROOT = '/var/www/userena.cl_calidad/static'

# Media 👉 Carpeta real donde se guardan archivos subidos
MEDIA_ROOT = '/var/www/userena.cl_calidad/media'

# Seguridad
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True 🔴 2. Falta HTTPS enforcement (muy recomendado) CICULS con balanceador llega solo puerto 80 al servidor

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
# X_FRAME_OPTIONS = 'DENY'
