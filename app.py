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


# ============================
# IMPORT WORKSHOP
# ============================

from modules.workshop.worshop_service import (
    generar_resumen_workshop
)

from modules.workshop.pdf_service import (
    generar_pdf_workshop
)



# ============================
# CONFIG
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
# CALENDARIO
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


    observaciones = st.text_area(
        "Observaciones / Comentarios",
        placeholder="Ingrese aclaraciones del proyecto..."
    )



    if st.button(
        "Generar calendario"
    ):


        if fecha_inicio.weekday() >= 5:


            st.error(
                "Debe iniciar un día hábil"
            )


        else:


            semanas = generar_semanas(
                fecha_inicio
            )


            periodo = generar_periodo(
                semanas
            )


            with st.spinner(
                "Generando calendario de implementación..."
            ):


                pdf = generar_pdf(
                    cliente,
                    semanas,
                    tipo_integracion,
                    periodo,
                    observaciones
                )


            st.success(
                "Calendario generado correctamente"
            )


            with open(
                pdf,
                "rb"
            ) as archivo:


                st.download_button(
                    "Descargar calendario PDF",
                    archivo,
                    file_name=f"Calendario - {cliente}.pdf"
                )




# ==================================================
# WORKSHOP
# ==================================================

if opcion == "Workshop Implementación":


    st.title(
        "Workshop Implementación Nubceo"
    )



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
            f"Obtención información {procesador}",
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



    criterios_conciliacion = st.multiselect(
        "Criterios de conciliación",
        [
            "NO CONCILIAMOS",
            "NO TENEMOS",
            "ID transacción",
            "Cupón",
            "Lote",
            "Terminal",
            "Sucursal",
            "Fecha",
            "Monto exacto",
            "Monto con tolerancia",
            "Autorización",
            "Últimos dígitos tarjeta",
            "Otro"
        ]
    )


    frecuencia_actual = st.selectbox(
        "Frecuencia actual",
        [
            "No conciliamos",
            "Diaria",
            "Semanal",
            "Mensual"
        ]
    )


    tiempo_conciliacion = st.selectbox(
        "Tiempo de conciliación",
        [
            "No aplica",
            "Menos de 1 hora",
            "1 a 4 horas",
            "1 día",
            "2 a 5 días",
            "Más de una semana"
        ]
    )


    frecuencia_deseada = st.selectbox(
        "Frecuencia deseada",
        [
            "Tiempo real",
            "Diaria automática",
            "Semanal automática"
        ]
    )


    porcentaje_conciliacion = st.slider(
        label="Porcentaje conciliado",
        min_value=0,
        max_value=100,
        value=80,
        step=5
    )


    no_conciliado = st.multiselect(
        "¿Qué ocurre con lo no conciliado?",
        [
            "Queda pendiente",
            "Revisión manual",
            "Ajuste contable",
            "No se analiza"
        ]
    )


    problemas = st.multiselect(
        "Problemas actuales",
        [
            "Trabajo manual",
            "Errores de conciliación",
            "Falta de visibilidad",
            "Demora operativa"
        ]
    )


    observaciones = st.text_area(
        "Observaciones del Workshop"
    )



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
            criterios_conciliacion,
            frecuencia_actual,
            tiempo_conciliacion,
            frecuencia_deseada,
            porcentaje_conciliacion,
            no_conciliado,
            problemas,
            observaciones
        )


        with st.spinner(
            "Generando Workshop Nubceo..."
        ):


            pdf = generar_pdf_workshop(
                datos
            )


        st.success(
            "Workshop generado correctamente"
        )


        with open(
            pdf,
            "rb"
        ) as archivo:


            st.download_button(
                "Descargar Workshop PDF",
                archivo,
                file_name=f"Workshop - {cliente}.pdf"
            )