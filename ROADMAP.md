# ROADMAP

## Objetivo actual

El objetivo es finalizar una primera versión funcional del Nubceo Implementation Generator para que pueda ser utilizada por los consultores de implementación.

Actualmente el Calendario y el Workshop funcionan correctamente y no deben modificarse salvo que sea necesario para implementar las mejoras indicadas a continuación.

---

# Prioridad 1 - Catálogos dinámicos

## Objetivo

Eliminar las listas fijas del Workshop.

Todos los selectores y multiselect deberán obtener sus opciones desde un archivo de configuración.

## Requerimientos

- Crear un archivo `config/workshop_options.json`.
- Todas las opciones del Workshop deberán leerse desde ese archivo.
- El consultor podrá agregar nuevas opciones desde la interfaz.
- Las nuevas opciones deberán guardarse automáticamente en `workshop_options.json`.
- No deberá ser necesario modificar el código para agregar nuevas opciones.
- No deberán permitirse opciones duplicadas.
- Mantener compatibilidad con la estructura actual del proyecto.

---

# Prioridad 2 - Workshop asistido por IA

## Objetivo

Permitir subir un documento de relevamiento en formato Word (.docx).

La IA deberá interpretar el contenido del documento y completar automáticamente el formulario del Workshop.

## Flujo esperado

Documento Word

↓

Interpretación mediante IA

↓

Completar automáticamente el formulario

↓

El consultor revisa la información

↓

Generación del PDF del Workshop

## Requerimientos

- Permitir subir archivos Word (.docx).
- Extraer automáticamente la información relevante.
- Completar los campos del Workshop.
- Mostrar un porcentaje de confianza para cada dato detectado.
- Permitir que el consultor modifique cualquier campo antes de generar el PDF.

---

## Importante

No modificar la arquitectura existente del proyecto.

No renombrar archivos.

No modificar el Calendario salvo que sea estrictamente necesario.

Mantener el diseño visual actual del Calendario y del Workshop.
