from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Static (solo desarrollo)
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media
MEDIA_ROOT = BASE_DIR / 'media'

# Base de datos (simple para desarrollo)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

