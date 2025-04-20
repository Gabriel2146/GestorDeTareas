Claro, aquí tienes un `README.md` completo y bien estructurado para tu proyecto **Gestor de Tareas en Django**, preparado para ser desplegado correctamente en **Render** sin necesidad de un `build.sh`:

---

## 🗂️ Gestor de Tareas - Django

Aplicación web desarrollada con **Django 5.2** para gestionar tareas, empleados y proyectos. Incluye funcionalidades CRUD, filtros por fechas y estados, y está lista para desplegarse en **Render**.

---

### 🚀 Funcionalidades principales

- Crear, listar, editar y eliminar:
  - ✅ Tareas
  - 🧑‍💼 Empleados
  - 🗂️ Proyectos
- Filtros por fecha de creación y estado de las tareas.
- Panel de administración de Django.
- Interfaz visual agradable usando Django templates + Bootstrap.
- Preparado para despliegue en Render (sin `build.sh`).

---

### 📦 Tecnologías utilizadas

- Python 3.11+
- Django 5.2
- SQLite (desarrollo) / PostgreSQL (producción opcional)
- Bootstrap (vía templates)
- Render (para el deploy)
- WhiteNoise (para servir archivos estáticos)
- Gunicorn (como WSGI server)

---

### 🛠️ Instalación local

1. **Clona el repositorio:**

```bash
git clone https://github.com/tu_usuario/GestorDeTareas.git
cd GestorDeTareas
```

2. **Crea y activa un entorno virtual:**

```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

3. **Instala las dependencias:**

```bash
pip install -r requirements.txt
```

4. **Ejecuta las migraciones:**

```bash
python manage.py migrate
```

5. **Crea un superusuario (opcional):**

```bash
python manage.py createsuperuser
```

6. **Ejecuta el servidor local:**

```bash
python manage.py runserver
```

Abre `http://localhost:8000` en tu navegador.

---

### 🧾 Estructura del proyecto

```
gestor_de_tareas/
├── core/                   # App principal con modelos y vistas
├── gestor_de_tareas/       # Configuración del proyecto
├── templates/              # Templates HTML
├── staticfiles/            # Archivos estáticos (generados)
├── manage.py
├── requirements.txt
└── README.md
```

---

### 🖥️ Despliegue en Render

#### 1. **Sube tu proyecto a GitHub.**

#### 2. **Configura Render:**

- Ve a [https://dashboard.render.com](https://dashboard.render.com).
- Crea un nuevo servicio → **Web Service**.
- Conecta tu repositorio de GitHub.

#### 3. **Configuración en Render:**

- **Build Command**:  
  ```bash
  pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
  ```

- **Start Command**:  
  ```bash
  gunicorn gestor_de_tareas.wsgi:application
  ```

- **Runtime**: Python 3.11+

- **Environment variables**:

  | Key                     | Value                                |
  |-------------------------|--------------------------------------|
  | `DEBUG`                 | `False`                              |
  | `SECRET_KEY`            | `una_clave_larga_y_segura`           |
  | `PYTHON_VERSION`        | `3.11.11`                            |
  | `DJANGO_SETTINGS_MODULE`| `gestor_de_tareas.settings`         |

---

### 📝 Procfile (opcional)

Si lo deseas, agrega un archivo `Procfile` en la raíz del proyecto con:

```
web: gunicorn gestor_de_tareas.wsgi:application
```

---

### 📸 Capturas (opcional)

Puedes incluir aquí imágenes de la interfaz de la app una vez funcionando.

---

### 👨‍💻 Autor

**Gabriel2146**  
GitHub: [github.com/Gabriel2146](https://github.com/Gabriel2146)

---
