# Proyecto Calidad – Django

Proyecto desarrollado con **Django** utilizando **entorno virtual (venv)** y control de versiones con **Git/GitHub**.

## 📌 Requisitos
- Python 3.10+ (probado con Python 3.13)
- pip
- Git

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
python3 -m venv venv

2️⃣ Activar entorno virtual
source venv/bin/activate

3️⃣ Instalar dependencias
pip install -r requirements.txt

▶️ Ejecutar el proyecto
python manage.py migrate

Crear usuario administrador
python manage.py createsuperuser


Iniciar servidor de desarrollo
python manage.py runserver






