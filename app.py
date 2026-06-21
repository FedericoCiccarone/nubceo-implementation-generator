import streamlit as st
from datetime import date


# ============================
# IMPORT CALENDARIO
# ============================

from modules.calendario.calendario_service import (
    generar_semanas,
    generar_periodo
)


from modules.calendario.pdf_service import (
    generar_pdf
)

from modules.workshop.pdf_service import (
    generar_pdf_workshop
)


# ============================
# IMPORT WORKSHOP
# ============================

from modules.workshop.worshop_service import (
    generar_resumen_workshop
)



# ============================
# CONFIG APP
# ============================

st.set_page_config(
    page_title="Nubceo Implementation Assistant",
    layout="wide"
)



# ============================
# MENU
# ============================

opcion = st.sidebar.radio(
    "Herramienta Nubceo",
    [
        "Calendario Implementación",
        "Workshop Implementación"
    ]
)




# ==================================================
# MODULO CALENDARIO
# ==================================================


if opcion == "Calendario Implementación":


    st.title(
        "📅 Calendario Implementación Nubceo"
    )


    cliente = st.text_input(
        "Cliente"
    )


    tipo_integracion = st.selectbox(
        "Tipo de integración",
        [
            "CSV",
            "API"
        ]
    )


    fecha_inicio = st.date_input(
        "Fecha inicio implementación",
        value=date.today()
    )



    if st.button(
        "Generar calendario"
    ):


        if fecha_inicio.weekday() >= 5:


            st.error(
                "La implementación debe iniciar un día hábil"
            )


        else:


            semanas = generar_semanas(
                fecha_inicio
            )


            periodo = generar_periodo(
                semanas
            )


            pdf = generar_pdf(
                cliente,
                semanas,
                tipo_integracion,
                periodo
            )


            with open(
                pdf,
                "rb"
            ) as archivo:


                st.download_button(
                    "Descargar calendario PDF",
                    archivo,
                    file_name=(
                        f"Calendario Implementación - "
                        f"{cliente} - {tipo_integracion}.pdf"
                    )
                )





# ==================================================
# MODULO WORKSHOP
# ==================================================


if opcion == "Workshop Implementación":


    st.title(
        "Workshop Implementación Nubceo"
    )


    # ----------------------------
    # DATOS CLIENTE
    # ----------------------------


    cliente = st.text_input(
        "Cliente"
    )


    canales = st.multiselect(
        "Canales de venta",
        [
            "Tienda Física",
            "Ecommerce"
        ]
    )


    erp = st.text_input(
        "ERP / Sistema de gestión"
    )


    origen_ventas = st.multiselect(
        "Origen de ventas",
        [
            "ERP",
            "Punto de Venta",
            "Ecommerce",
            "Base de datos",
            "Archivo"
        ]
    )


    # ----------------------------
    # PROCESADORES
    # ----------------------------


    st.subheader(
        "Procesadores de pago"
    )


    procesadores = st.multiselect(
        "Procesadores utilizados",
        [
            "Fiserv",
            "Prisma",
            "Mercado Pago",
            "Payway",
            "Getnet",
            "Otro"
        ]
    )


    detalle_procesadores = []


    for procesador in procesadores:


        metodo = st.selectbox(
            f"¿Cómo obtiene información de {procesador}?",
            [
                "Portal",
                "CSV",
                "API",
                "SFTP",
                "Otro"
            ]
        )


        detalle_procesadores.append(
            {
                "nombre": procesador,
                "conexion": metodo
            }
        )


    # ----------------------------
    # CONCILIACION ACTUAL
    # ----------------------------


    st.subheader(
        "Conciliación actual"
    )


    conciliacion = st.selectbox(
        "¿Cómo concilian actualmente?",
        [
            "Manual",
            "Excel",
            "Desarrollo propio",
            "Otro proveedor"
        ]
    )


    tareas_manuales = st.multiselect(
        "Procesos manuales actuales",
        [
            "Descarga archivos",
            "Cruce de ventas y pagos",
            "Control promociones",
            "Revisión diferencias",
            "Reportes manuales"
        ]
    )


    problemas = st.multiselect(
        "Problemas actuales",
        [
            "Trabajo manual",
            "Demora operativa",
            "Errores de conciliación",
            "Falta de visibilidad",
            "Diferencias sin resolver"
        ]
    )


    # ----------------------------
    # GENERAR WORKSHOP
    # ----------------------------


    if st.button(
        "Generar Workshop"
    ):


        datos = generar_resumen_workshop(
            cliente,
            canales,
            erp,
            origen_ventas,
            detalle_procesadores,
            conciliacion,
            tareas_manuales,
            problemas
        )


        pdf = generar_pdf_workshop(
            datos
        )


        with open(
            pdf,
            "rb"
        ) as archivo:


            st.download_button(
                "Descargar Workshop PDF",
                archivo,
                file_name=(
                    f"Workshop - {cliente}.pdf"
                )
            )