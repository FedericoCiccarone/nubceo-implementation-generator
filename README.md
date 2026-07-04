# Nubceo Implementation Generator

Generador de documentación para implementaciones de Nubceo.

Actualmente permite generar:

- 📅 Calendario de Implementación (PDF)
- 📋 Workshop de Relevamiento (PDF)

---

# Requisitos

- Windows 10 / Windows 11
- Python 3.11 o superior
- Google Chrome instalado
- Git (opcional)

---

# Instalación

La primera vez únicamente ejecutar:

```bash
setup.bat
```

Este script realiza automáticamente:

- Creación del entorno virtual (`venv`)
- Instalación de todas las dependencias
- Instalación de los navegadores de Playwright
- Configuración inicial del proyecto

Cuando finalice la instalación el proyecto estará listo para utilizarse.

---

# Ejecutar la aplicación

Una vez instalado, simplemente ejecutar:

```bash
run.bat
```

Este script:

- Activa el entorno virtual
- Inicia Streamlit
- Abre la aplicación en el navegador

---

# Estructura del proyecto

```
nubceo-implementation-generator/

│
├── app.py
├── setup.bat
├── run.bat
├── requirements.txt
│
├── config/
│   └── workshop_options.json
│
├── modules/
│
│   ├── calendario/
│   │
│   ├── workshop/
│   │
│   └── output/
│
└── output/
```

---

# Funcionalidades

## Calendario

Genera automáticamente un calendario de implementación en formato PDF.

Incluye:

- Calendario de 8 semanas
- Cálculo automático de días hábiles
- Tipo de integración (API / CSV)
- Observaciones del consultor

---

## Workshop

Genera un Workshop tipo AS-IS en formato PDF.

Permite relevar:

- Canales
- ERP
- Procesadores
- Métodos de obtención
- Conciliación
- Procesos manuales
- Problemas
- Observaciones

---

# Catálogos dinámicos

Las opciones de los selectores se almacenan en:

```
config/workshop_options.json
```

Los consultores pueden agregar nuevas opciones directamente desde la aplicación sin modificar el código.

---

# Tecnologías utilizadas

- Python
- Streamlit
- Jinja2
- Playwright
- HTML / CSS
- JSON

---

# Próximas funcionalidades

Versión 1.1

- Integración con Gemini AI
- Carga automática de formularios de relevamiento
- Autocompletado del Workshop mediante IA

---

# Soporte

Proyecto desarrollado para el equipo de Implementaciones de Nubceo.
