"""
WSGI config for calidad project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

# Base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables desde .env
load_dotenv(BASE_DIR / ".env")

# Determinar entorno (dev por defecto)
env = os.getenv("ENVIRONMENT", "dev")

# Definir settings según entorno
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    f"calidad.settings.{env}"
)

application = get_wsgi_application()
