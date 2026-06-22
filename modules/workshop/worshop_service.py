def generar_resumen_workshop(
    cliente,
    canales,
    erp,
    origen_ventas,
    procesadores,
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
):


    datos = {


        "cliente": cliente,


        "canales": canales,


        "erp": erp,


        "origen_ventas": origen_ventas,


        "procesadores": procesadores,


        "conciliacion": conciliacion,


        "tareas_manuales": tareas_manuales,


        "resultado_conciliacion": {


            "criterios": criterios_conciliacion,


            "frecuencia_actual": frecuencia_actual,


            "tiempo": tiempo_conciliacion,


            "frecuencia_deseada": frecuencia_deseada,


            "porcentaje": porcentaje_conciliacion,


            "no_conciliado": no_conciliado


        },


        "problemas": problemas,


        "observaciones": observaciones


    }


    return datos