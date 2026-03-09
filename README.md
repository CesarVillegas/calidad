# Proyecto Calidad – Django

Proyecto desarrollado con **Django** utilizando **entorno virtual (venv)** y control de versiones con **Git/GitHub**.

## 📌 Requisitos
- Python 3.10+ (probado con Python 3.13)
- pip
- Git


### Django

* Django 5.2 fue lanzado el 2 de abril de 2025 y está designado como release LTS, con soporte de seguridad garantizado por al menos 3 años. Django
* La versión patch más reciente disponible hoy es **Django 5.2.12**



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


## ⚙️ Configuración del entorno

### 1️⃣ Crear entorno virtual

```bash

1️⃣ Clonar el repositorio
git clone <url-del-repositorio>

2️⃣ Instalar y Activar entorno virtual
python3 -m venv venv
source venv/bin/activate 
which python

3️⃣ Instalar dependencias
pip install -r requirements.txt

▶️ Ejecutar el proyecto
python manage.py migrate

Crear usuario administrador
python manage.py createsuperuser

Iniciar servidor de desarrollo
python manage.py runserver

```

Django y MySQL 5.7

Django 4.2 fue la última versión en soportar MySQL 5.7
Django 5.0 en adelante requiere MySQL 8.0 como mínimo

Entonces si tu servidor tiene MySQL 5.7.19, no puedes usar Django 5.x.
Tabla resumen:
Django      MySQL mínimo
4.2         LTS5.7 ✅
5.0         8.0 ✅
5.1         8.0 ✅









 python manage.py createsuperuser

Username (leave blank to use 'desarrollador'): cesar
Email address: cevillegas@userena.cl
Password: qwe123


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


Buenas prácticas desde ahora

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
    │   ├── settings.py
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
        ├── tests.py
        ├── urls.py
        └── views.py

~~~


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