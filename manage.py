#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv


def main():
    """Run administrative tasks."""

    # Base del proyecto
    BASE_DIR = Path(__file__).resolve().parent

    # Cargar variables desde .env
    load_dotenv(BASE_DIR / ".env")

    # Determinar entorno (dev por defecto)
    env = os.getenv("ENVIRONMENT", "dev")

    # Definir settings según entorno
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        f"calidad.settings.{env}"
    )

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? "
            "Did you forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()