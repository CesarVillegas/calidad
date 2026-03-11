from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = ['tudominio.com', 'www.tudominio.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # o postgresql
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# Seguridad
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True