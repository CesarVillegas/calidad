from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError
from .validators import validar_extension_imagen, validar_resolucion_banner, validar_resolucion_banner_mobile



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

    # 📱 Mobile (nuevo)
    imagen_mobile = models.ImageField(
        upload_to='banners/mobile/',
        validators=[validar_extension_imagen, validar_resolucion_banner_mobile],
        blank=True,
        null=True,
        help_text='Mobile: recomendado 720×960px.'
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




class CategoriaIndicador(models.Model):
    nombre = models.CharField(max_length=150,help_text="Nombre de la categoría (ej: Docencia, Investigación)")
    orden = models.PositiveIntegerField(default=1,help_text="Orden de visualización de la categoría")
    publicado = models.BooleanField(default=True,help_text="Indica si la categoría se muestra")

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['orden', 'id']



class Indicador(models.Model):
    categoria = models.ForeignKey(
        CategoriaIndicador,
        on_delete=models.CASCADE,
        related_name='indicadores'
    )

    titulo = models.CharField(max_length=150)
    valor = models.CharField(max_length=150)
    sufijo = models.CharField(max_length=10, blank=True)
    descripcion = models.TextField(blank=True, max_length=255)
    subtitulo = models.CharField(max_length=255,blank=True,null=True)
    icono = models.ImageField(upload_to='indicadores/estatico/')            # Imagen base (SIEMPRE existe)

    # GIF opcional (solo para destacados)
    icono_gif = models.ImageField(
        upload_to='indicadores/gif/',
        null=True,
        blank=True
    )

    orden = models.PositiveIntegerField(default=1)                                  # Orden dentro de la categoría
    publicado = models.BooleanField(default=True)
    destacado = models.BooleanField(default=False,help_text="Mostrar en el home")   # Destacados en home
    # Orden en home (NO único, puede repetirse)
    orden_destacado = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Orden en el home"
    )

    # clean() es un hook de validación del modelo.
    # Se ejecuta cuando se llama full_clean() (por ejemplo en ModelForms o Django Admin).
    # NO se ejecuta automáticamente al hacer save().
    def clean(self):
        errors = {}

        # 🔹 Regla 1: orden obligatorio si es destacado
        if self.destacado and self.orden_destacado is None:
            errors['orden_destacado'] = 'Debe definir un orden si el indicador es destacado.'

        # 🔹 Regla 2: gif obligatorio si es destacado
        if self.destacado and not self.icono_gif:
            errors['icono_gif'] = 'Debe subir un GIF si el indicador es destacado.'

        # 🔹 Limpieza lógica
        if not self.destacado:
            self.orden_destacado = None

        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return f"{self.titulo} - {self.valor}{self.sufijo}"

    # 🔹 Helper para vistas
    def get_icono_home(self):
        if self.destacado and self.icono_gif:
            return self.icono_gif.url
        return self.icono.url

    class Meta:
        ordering = ['orden', 'id']
        constraints = [
            # Solo regla realmente necesaria
            models.CheckConstraint(
                check=Q(destacado=False) | Q(icono_gif__isnull=False),
                name='gif_required_if_destacado'
            ),
        ]