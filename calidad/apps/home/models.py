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
    url_externa = models.BooleanField(default=False)            # abre en _blank

    # Control de publicación
    activo      = models.BooleanField(default=True)
    orden       = models.PositiveSmallIntegerField(default=0)   # para ordenar el carrusel
    fecha_inicio = models.DateField(null=True, blank=True)      # publicación programada
    fecha_fin    = models.DateField(null=True, blank=True)

    # Auditoría
    creado_en      = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['orden', '-creado_en']
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.titulo or f'Banner #{self.pk}'