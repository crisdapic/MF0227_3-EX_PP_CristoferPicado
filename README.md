# Sistema de Gestión de Incidencias Técnicas (Helpdesk)

## Descripción del proyecto

Este proyecto desarrolla un sistema de gestión de incidencias técnicas (Helpdesk), aplicando los conocimientos adquiridos en el curso de programación de Fundación Esplai.

Se trabajan los contenidos correspondientes a las unidades formativas **UF2404, UF2405 y UF2406**, integrando programación orientada a objetos, desarrollo web con Django y control de versiones con Git.

---

## 1. Arquitectura del proyecto y relación con las UF

### UF2404 - Principios de programación orientada a objetos

Implementada en el módulo independiente `core_modelos.py`.

Se aplican los siguientes conceptos:

- Encapsulación.
- Herencia mediante las clases `TicketHardware` y `TicketSoftware`.
- Polimorfismo.
- Gestión de excepciones personalizadas mediante `EstadoInvalidoError`.
- Validación de transiciones de estado.

### UF2405 - Desarrollo web con Django y ORM

Implementada principalmente en la aplicación `incidencias`.

Incluye:

- Modelos relacionales `Tecnico` e `Incidencia`.
- Relaciones entre técnicos e incidencias mediante claves foráneas.
- Formularios basados en modelos (`ModelForm`).
- Vistas para listar y crear incidencias.
- Plantillas HTML con Bootstrap 5.
- Panel de administración de Django.
- Gestión de estados y prioridades.

### UF2406 - Control de versiones y documentación

Gestionado mediante Git y GitHub.

Se utiliza un flujo de trabajo con las ramas:

- `main`: rama principal del proyecto.
- `desarrollo`: rama de trabajo y evolución del proyecto.

Se utilizan commits descriptivos para registrar los cambios y mantener un historial del desarrollo.

---

## 2. Estructura del proyecto

```text
helpdesk_project/
│
├── helpdesk_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── incidencias/
│   ├── migrations/
│   ├── templates/
│   │   └── incidencias/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── tickets/
│
├── core_modelos.py
├── manage.py
├── requirements.txt
├── pruebas.txt
├── README.md
└── .gitignore
```

La carpeta `venv/` y la base de datos local SQLite no se incluyen en el control de versiones.

---

## 3. Requisitos previos

Para ejecutar el proyecto se necesita:

- Python 3.
- pip.
- Git.
- Un entorno virtual de Python.
- Las dependencias indicadas en `requirements.txt`.

---

## 4. Instalación y configuración

### 4.1. Clonar el repositorio

```bash
git clone https://github.com/crisdapic/MF0227_3-EX_PP_CristoferPicado.git
```

Entrar en la carpeta que contiene el archivo `manage.py`.

### 4.2. Crear el entorno virtual

En Windows PowerShell:

```powershell
python -m venv venv
```

### 4.3. Activar el entorno virtual

```powershell
.\venv\Scripts\Activate.ps1
```

### 4.4. Instalar las dependencias

```powershell
pip install -r requirements.txt
```

### 4.5. Preparar la base de datos

```powershell
python manage.py migrate
```

### 4.6. Crear un usuario administrador

```powershell
python manage.py createsuperuser
```

Seguir las instrucciones para configurar el usuario y la contraseña.

---

## 5. Ejecución del proyecto

Para iniciar el servidor de desarrollo:

```powershell
python manage.py runserver
```

Abrir el navegador y acceder a:

- Aplicación web: http://127.0.0.1:8000/
- Administración Django: http://127.0.0.1:8000/admin/

El servidor se ejecuta en modo desarrollo local.

---

## 6. Pruebas unitarias

El proyecto incorpora pruebas automatizadas mediante el sistema de testing de Django.

Las pruebas se encuentran en:

```text
incidencias/tests.py
```

Para ejecutar las pruebas de la aplicación:

```powershell
python manage.py test incidencias
```

Para ejecutar todas las pruebas del proyecto:

```powershell
python manage.py test
```

### Resultado de las pruebas

En la última ejecución de las pruebas generales se obtuvo:

```text
Found 7 test(s).
Ran 7 tests in 0.004s

OK
```

Las siete pruebas finalizaron correctamente.

Se comprueban aspectos como:

- Creación de técnicos.
- Creación de incidencias.
- Asignación de técnicos.
- Fecha de creación.
- Representación de los modelos.
- Validación de formularios.
- Campos obligatorios.

El documento `pruebas.txt` recoge el plan de pruebas y los resultados obtenidos.

---

## 7. Control de versiones

El proyecto utiliza Git para controlar los cambios realizados durante el desarrollo.

Las principales ramas son:

- `main`
- `desarrollo`

Para consultar el estado del repositorio:

```bash
git status
```

Para consultar el historial:

```bash
git log --oneline
```

Para registrar cambios:

```bash
git add .
git commit -m "Descripción de los cambios"
```

Para subir los cambios a GitHub:

```bash
git push origin desarrollo
```

---

## 8. Autoría

Proyecto desarrollado como ejercicio práctico del curso de programación de Fundación Esplai, correspondiente a las unidades formativas UF2404, UF2405 y UF2406.

**Proyecto:** Sistema de Gestión de Incidencias Técnicas (Helpdesk).

**Tecnologías principales:** Python, Django, SQLite, HTML, Bootstrap 5 y Git.