from django.db import models
from .validators import validar_extension_imagen, validar_resolucion_banner

# Create your models here.
class Banner(models.Model):
    titulo      = models.CharField(max_length=200, blank=True)
    subtitulo   = models.CharField(max_length=300, blank=True)
    descripcion = models.TextField(blank=True)

    # Imagen del banner con validaciones personalizadas
    imagen = models.ImageField(
        upload_to='banners/',
        validators=[validar_extension_imagen, validar_resolucion_banner],
        help_text='JPG, PNG o WEBP. Resolución recomendada: 1920×600px. Mínimo: 1200×375px.'
    )
    imagen_alt  = models.CharField(max_length=200, blank=True)  # accesibilidad

    # Enlace (opcional — el banner puede ser clickeable)
    url         = models.URLField(blank=True)
    url_texto   = models.CharField(max_length=100, blank=True)  # texto del botón CTA
    url_externa = models.BooleanField(default=True)            # abre en _blank

    # Control de publicación
    publicado   = models.BooleanField(default=True)
    orden       = models.PositiveSmallIntegerField(default=0)   # para ordenar el carrusel

    class Meta:
        ordering = ['orden', 'publicado']
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.titulo or f'Banner #{self.pk}'



class Indicador(models.Model):
    titulo = models.CharField(
        max_length=150,
        help_text="Nombre del indicador (ej: Retención de primer año)"
    )

    valor = models.CharField(
        max_length=150,
        help_text="Valor a mostrar (ej: 84,6 o 2do). No incluir el símbolo % si usas el sufijo."
    )

    sufijo = models.CharField(
        max_length=10,
        blank=True,
        help_text="Símbolo opcional (ej: %, pts). Déjalo vacío si no aplica."
    )

    descripcion = models.TextField(
        blank=True,
        max_length=255,
        help_text="Descripción breve del indicador"
    )

    subtitulo = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Texto adicional (ej: Cohorte 2024)"
    )

    icono = models.ImageField(
        upload_to='indicadores/',
        help_text="Ícono representativo (SVG o PNG recomendado)"
    )

    orden = models.PositiveIntegerField(
        default=1,
        help_text="Define el orden de aparición (menor = primero)"
    )

    publicado = models.BooleanField(
        default=True,
        help_text="Indica si el indicador se muestra en el sitio"
    )

    def __str__(self):
        return f"{self.titulo} - {self.valor}{self.sufijo}"

    class Meta:
        ordering = ['orden']