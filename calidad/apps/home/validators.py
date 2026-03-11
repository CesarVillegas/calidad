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

    ANCHO_MIN, ALTO_MIN = 1200, 400
    ANCHO_MAX, ALTO_MAX = 3840, 1080

    if ancho < ANCHO_MIN or alto < ALTO_MIN:
        raise ValidationError(
            f'Resolución mínima {ANCHO_MIN}×{ALTO_MIN}px. '
            f'Imagen subida: {ancho}×{alto}px.'
        )
    if ancho > ANCHO_MAX or alto > ALTO_MAX:
        raise ValidationError(
            f'Resolución máxima {ANCHO_MAX}×{ALTO_MAX}px. '
            f'Imagen subida: {ancho}×{alto}px.'
        )