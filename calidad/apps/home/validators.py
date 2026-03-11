# home/validators.py
import os
from django.core.exceptions import ValidationError


def validar_extension_imagen(value):
    ext = os.path.splitext(value.name)[1].lower()
    extensiones_validas = ['.jpg', '.jpeg', '.png', '.webp']
    if ext not in extensiones_validas:
        raise ValidationError(
            f'Extensión "{ext}" no permitida. Use: {", ".join(extensiones_validas)}'
        )


def validar_resolucion_banner(value):
    from PIL import Image
    imagen = Image.open(value)
    ancho, alto = imagen.size

    resoluciones_validas = [
        (1920, 600),
        (1200, 375),
    ]

    if (ancho, alto) not in resoluciones_validas:
        raise ValidationError(
            f'Resolución no permitida ({ancho}×{alto}px). '
            f'Use: 1920×600px o 1200×375px.'
        )