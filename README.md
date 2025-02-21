# Django CRUD Auth - Gestor de Tareas

Una aplicación web desarrollada con Django que permite gestionar tareas personales con sistema de autenticación de usuarios.

## 🚀 Características

- Sistema de autenticación (registro, login, logout)
- Gestión completa de tareas (CRUD):
  - ✨ Crear tareas
  - 📋 Listar tareas
  - ✏️ Editar tareas
  - ✅ Marcar como completadas
  - 🗑️ Eliminar tareas
- 🔒 Protección de rutas
- 📱 Diseño responsive con Bootstrap

## 📋 Requisitos Previos

- Python 3.13.1 o superior
- pip (gestor de paquetes de Python)

## 🛠️ Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/Leonardoih/django-crud-auth.git
cd django-crud-auth
```

2. **Crear y activar entorno virtual**
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Realizar migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario (opcional)**
```bash
python manage.py createsuperuser
```

6. **Iniciar servidor**
```bash
python manage.py runserver
```

## 📝 Uso

1. Navega a `http://127.0.0.1:8000/`
2. Regístrate como nuevo usuario o inicia sesión
3. Comienza a gestionar tus tareas:
   - Crea nuevas tareas
   - Marca tareas como importantes
   - Completa tareas
   - Elimina tareas

## 🗂️ Estructura del Proyecto

```
django-crud-auth/
├── tasks/                # Aplicación principal
│   ├── templates/       # Plantillas HTML
│   ├── models.py        # Modelos de datos
│   ├── forms.py         # Formularios
│   ├── views.py         # Vistas
│   └── urls.py         # URLs de la aplicación
├── djangocrud/          # Configuración del proyecto
└── manage.py           # Script de gestión
```

## 🛠️ Tecnologías Utilizadas

- Django 5.1.6
- Bootstrap 5
- SQLite3
- Python 3.13.1

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## ✨ Contribuir

1. Haz un Fork del proyecto
2. Crea tu rama de función (`git checkout -b feature/NuevaFuncion`)
3. Haz commit de tus cambios (`git commit -m 'Añadir nueva función'`)
4. Haz Push a la rama (`git push origin feature/NuevaFuncion`)
5. Abre un Pull Request

## 👥 Autor

* **Leonardo Izquierdo** - *Trabajo Inicial* - [Leonardoih](https://github.com/Leonardoih)

## 🙏 Agradecimientos y Créditos

Este proyecto fue desarrollado siguiendo el tutorial ["Django CRUD con Autenticación y Despliegue Gratuito"](https://www.youtube.com/watch?v=e6PkGDH4wWA) creado por Fazt Tech.

* **Fazt Tech** - *Tutorial Original*
  * Canal de YouTube: [Fazt Tech](https://www.youtube.com/@FaztTech)
  * Duración del tutorial: 3:18:12
  * Título del tutorial: Django CRUD con Autenticación y Despliegue Gratuito (Login, Register, Rutas protegidas, y más)

Este proyecto es una implementación educativa basada en el contenido enseñado por Fazt Tech. Todos los créditos del diseño y conceptos originales corresponden a su autor.