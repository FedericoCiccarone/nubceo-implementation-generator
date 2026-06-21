def generar_resumen_workshop(
    cliente,
    canales,
    erp,
    origen_ventas,
    procesadores,
    conciliacion,
    tareas_manuales,
    problemas
):


    datos = {

        "cliente": cliente,

        "canales": canales,

        "erp": erp,

        "origen_ventas": origen_ventas,

        "procesadores": procesadores,

        "conciliacion": conciliacion,

        "tareas_manuales": tareas_manuales,

        "problemas": problemas

    }


    return datos