# Sistema de gestión de Incidencias Técnicas (HelpDesk)

En este proyecto se implementan los conocimientos de los distintos m+odulos del curso de programación orientada a objetos de Fundación Esplai, donde se ponen en práctica los contenidos de las distintas seccions del curso **UF2404**,  **UF2405** y **UF2406**.

---

## 1. Arquitectura del Proyecto y Relación de UF
* **UF2404 (Principios de POO):** Implementada en el módulo independiente `core_modelos.py`, donde se aplican encapsulación, herencia (`TicketHardware`, `TicketSoftware`), polimorfismo  y gestión de excepciones personalizadas (`EstadoInvalidoError`).
* **UF2405 (Desarrollo Web con Django y ORM):** Implementada en la app 'incidencias', estructurada con Modelos relacionales (`Tecnico`, `Incidencia`), panel de administración avanzado, vistas basadas en clases (`ListView`, `CreateView`), formularios y plantillas con Bootstrap 5.
* **UF2406 (Control de Versiones y Documentación):** Gestionado mediante Git con un flujo estructurado de ramas (`main` y `desarrollo`), commits atómicos descriptivos y documentación técnica integral.

---

## 2. Instrucciones de Instalación y Despliegue Local

Sigue estos pasos en tu terminal para poner en marcha el entorno de desarrollo:

### 1. Clonar el repositorio y cambiar a la rama de desarrollo
```bash
git clone [https://github.com/crisdapic/MF0227_3-EX_PP_CristoferPicado.git](https://github.com/crisdapic/MF0227_3-EX_PP_CristoferPicado.git)
cd helpdesk_project
git checkout desarrollo