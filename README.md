# Proyecto Calidad – Django

Proyecto desarrollado con **Django** utilizando **entorno virtual (venv)** y control de versiones con **Git/GitHub**.

## 📌 Requisitos
- Python 3.10+ - `pip` - `Git`


### Django

* Django 5.2 fue lanzado el 2 de abril de 2025 y está designado como **release LTS**, con soporte de seguridad garantizado por al menos 3 años. 
* Django La versión patch más reciente disponible hoy es **Django 5.2.12**


## ⚙️ Configuración del entorno

```bash
# 1️⃣ Clonar el repositorio
git clone <url-del-repositorio>

# 2️⃣ Instalar y Activar entorno virtual
python3 -m venv venv
source venv/bin/activate 
which python

# 3️⃣ Instalar dependencias
pip install -r requirements.txt

# 8️⃣ Verificar versión instalada
python -m django --version

# Iniciar servidor de desarrollo
python manage.py runserver
```

### Configuración por entornos (settings/) Desarrollo y Producción

El archivo **settings.py** por defecto se reemplaza por un paquete con tres módulos:

```
calidad/
└── settings/
    ├── base.py   ← configuración común a todos los entornos
    ├── dev.py    ← sobreescribe base.py para desarrollo local
    └── prod.py   ← sobreescribe base.py para producción
```

* **base.py** contiene todo lo que es compartido: INSTALLED_APPS, TEMPLATES, MIDDLEWARE, etc.
* **dev.py** importa base y añade configuración local: DEBUG = True, base de datos SQLite, django-debug-toolbar, etc.
* **prod.py** importa base y endurece la configuración: DEBUG = False, base de datos PostgreSQL, variables de entorno para secrets, ALLOWED_HOSTS, etc.


## Activar el Entorno Correcto

### manage.py (desarrollo local):

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calidad.settings.dev')


### wsgi.py (producción — manage.py no se usa en producción):

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calidad.settings.prod')


## base.py — Puntos clave y variables de entorno

Estructura recomendada de base.py

~~~python
from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # ⚠️ tres niveles arriba por el paquete settings/

load_dotenv(BASE_DIR / '.env')
~~~


Variables críticas que siempre van en **.env**

~~~
# .env
SECRET_KEY=django-insecure-xxxxxxxxxxxxxxxxxxxx
DEBUG=True

# Base de datos
DB_NAME=calidad_db
DB_USER=postgres
DB_PASSWORD=supersecret
DB_HOST=localhost
DB_PORT=5432

# Correo (si aplica)
EMAIL_HOST_USER=no-reply@dominio.cl
EMAIL_HOST_PASSWORD=password
~~~

## Dependencia necesaria

~~~bash
pip install python-dotenv
~~~

O con el enfoque más robusto usando django-environ:

~~~bash
pip install django-environ  # maneja cast de tipos, listas y URLs de DB automáticamente
~~~


## Datos
Flujo completo antes del primer migrate
1. Definir modelos        → models.py, validators.py
2. Makemigrations         → genera archivos de migración
3. Migrate                → aplica cambios a la BD
4. Createsuperuser        → crea el usuario admin
5. Runserver              → verificar en el admin



~~~bash
# 1. Verificar que el modelo no tenga errores de sintaxis
python manage.py check
# 2. Generar las migraciones
python manage.py makemigrations
# o específico por app
python manage.py makemigrations home
# 3. Ver qué va a ejecutar (opcional pero recomendado), Muestra el SQL que se ejecutará — útil para revisar antes de tocar la BD.
python manage.py sqlmigrate home 0001
# 4. Aplicar migraciones
python manage.py migrate
# 5. Crear superusuario
python manage.py createsuperuser
```
```
Username: admin
Email: admin@userena.cl
Password: ********
~~~

    Username (leave blank to use 'desarrollador'): cesar
    Email address: cevillegas@userena.cl
    Password: qwe123


Si ya hiciste migrate antes y ahora agregaste campos nuevos

~~~bash
# Solo estos dos pasos
python manage.py makemigrations
python manage.py migrate
# No es necesario volver a crear el superusuario, ya existe en la BD.

# Ver estado de migraciones en cualquier momento
python manage.py showmigrations
# Una migración con [ ] significa que existe el archivo pero no se ha aplicado a la BD — falta correr migrate.
~~~


### Warning

> home.Banner: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
        HINT: Configure the DEFAULT_AUTO_FIELD setting or the HomeConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.

Es solo un warning, no un error — pero conviene resolverlo. La solución más limpia es en base.py:

Opción 1 — Global en base.py (recomendado)

~~~bash
# Aplica a todas las apps del proyecto de una sola vez.
# settings/base.py

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django 3.2+ cambió el default a BigAutoField pero no lo fuerza en proyectos existentes para no romper migraciones 
~~~


#****************************************************************************************************************
# APUNTES
#****************************************************************************************************************
## Django y MySQL 5.7

Django 4.2 fue la última versión en soportar MySQL 5.7
Django 5.0 en adelante requiere MySQL 8.0 como mínimo

Entonces si tu servidor tiene MySQL 5.7.19, no puedes usar Django 5.x.
Tabla resumen:
Django      MySQL mínimo
4.2         LTS5.7 ✅
5.0         8.0 ✅
5.1         8.0 ✅



# Crear la rama y cambiarte a ella en un solo comando
git checkout -b testing

# Verificar que estás en la rama correcta
git branch






## Templates

1️⃣ Crear estructura de templates
2️⃣ Crear base.html
3️⃣ Crear index.html

    home/
    ├── templates/
    │   └── home/
    │       ├── base.html
    │       └── index.html


4️⃣ Ajustar la vista para usar templates

    def index(request):
        return render(request, 'home/index.html')

5️⃣ Verificar configuración de templates

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],   # correcto para templates dentro de apps
            'APP_DIRS': True,
            ...
        },
    ]


6️⃣ Probar en el navegador


## Buenas prácticas desde ahora

✔ Un base.html por proyecto
✔ Templates por app (home/)
✔ Usar {% extends %} y {% block %}
✔ No mezclar lógica en templates


## Bootstrap

1️⃣ Configurar archivos estáticos (settings)


    STATIC_URL = 'static/'

    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]


2️⃣ Crear estructura de static

Desde la raíz del proyecto Django (donde está manage.py):
mkdir -p static/css

    calidad/
    ├── static/
    │   └── css/
    │       └── styles.css


3️⃣ Crear archivo CSS propio

Archivo: static/css/styles.css


4️⃣ Modificar base.html para Bootstrap

Archivo: home/templates/home/base.html


🧠 Buenas prácticas

* Bootstrap por CDN en desarrollo
* CSS propio separado
* {% load static %} siempre arriba
* Navbar en base.html

Un CSS global + CSS por app cuando sea necesario
✅ es la mejor práctica en proyectos reales


### Estructura Ideal

~~~
proyecto_calidad/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── venv/                     ← entorno virtual (NO versionado)
│
├── calidad/                  ← proyecto Django 
    │
    ├── static/                   ← static GLOBAL del proyecto
    │   ├── css/
    │   │   └── base.css           ← estilos institucionales USERENA
    │   ├── img/
    │   │   └── logo-userena.png   ← logo institucional (opcional)
    │   └── js/
    │
    ├── templates/                ← templates GLOBAL
    │   ├── base.html              ← layout base (HTML principal)
    │   ├── includes/
    │   │   ├── header.html        ← navbar institucional
    │   │   └── footer.html        ← footer institucional
    │   └── home/
    │       └── index.html         ← template de la app home
    │
    ├── manage.py
    │
    ├── db.sqlite3                 ← solo desarrollo (NO producción)
    │
    ├── calidad/                   ← proyecto Django (configuración)
    │   ├── __init__.py
    │   ├── settings/
    │   │   ├── base.py   ← configuración común a todos los entornos
    │   │   ├── dev.py    ← sobreescribe base.py para desarrollo local
    │   │   └── prod.py   ← sobreescribe base.py para producción
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    └── home/                      ← app Django
        ├── migrations/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── validators.py   ← aquí van los validadores
        ├── tests.py
        ├── urls.py
        └── views.py

~~~


## 📂 Estructura del proyecto

    proyecto_calidad/
    ├── venv/ # Entorno virtual (no versionado)
    ├── calidad/ # Proyecto Django
    │ ├── manage.py
    │ └── calidad/
    │ ├── settings.py
    │ ├── urls.py
    │ ├── wsgi.py
    │ └── asgi.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md

🧠 Beneficios reales

✔ Arquitectura limpia
✔ Mantenible
✔ Preparado para múltiples apps
✔ Fácil de documentar
✔ Estándar Django profesional


🧠 Regla importante de Django Templates

📌 Cada archivo template es independiente
Aunque base.html tenga {% load static %}, NO se hereda a:

* include
* extend
* partials

👉 Cada template que use {% static %} debe cargarlo.


📱 OBJETIVO RESPONSIVE (mobile)

En pantallas pequeñas (<992px) queremos:

Header
* Logo visible
* Menú oculto
* Botón ☰ (hamburger)
* Menú desplegable vertical

Footer

* Columnas → stack vertical
* Espaciado claro
* Títulos legibles
* Links cómodos para touch



## Adminitración de Banners

pip install Pillow