from datetime import timedelta


MESES = {
    1: "ENE",
    2: "FEB",
    3: "MAR",
    4: "ABR",
    5: "MAY",
    6: "JUN",
    7: "JUL",
    8: "AGO",
    9: "SEP",
    10: "OCT",
    11: "NOV",
    12: "DIC",
}


def sumar_dias_habiles(fecha, dias):
    fecha_actual = fecha
    agregados = 0

    while agregados < dias:
        fecha_actual += timedelta(days=1)

        if fecha_actual.weekday() < 5:
            agregados += 1

    return fecha_actual



def formato_fecha(fecha):

    return f"{fecha.day}{MESES[fecha.month]}"



def generar_semanas(fecha_inicio):

    semanas = []

    inicio = fecha_inicio


    for numero in range(1,9):

        fin = sumar_dias_habiles(inicio, 4)


        semanas.append({
            "semana": numero,
            "inicio": formato_fecha(inicio),
            "fin": formato_fecha(fin)
        })


        inicio = sumar_dias_habiles(fin, 1)


    return semanas

def generar_periodo(semanas):

    meses = {
        "ENE": "Enero",
        "FEB": "Febrero",
        "MAR": "Marzo",
        "ABR": "Abril",
        "MAY": "Mayo",
        "JUN": "Junio",
        "JUL": "Julio",
        "AGO": "Agosto",
        "SEP": "Septiembre",
        "OCT": "Octubre",
        "NOV": "Noviembre",
        "DIC": "Diciembre"
    }


    inicio = semanas[0]["inicio"]
    fin = semanas[-1]["fin"]


    mes_inicio = ''.join(
        filter(str.isalpha, inicio)
    )

    mes_fin = ''.join(
        filter(str.isalpha, fin)
    )


    return (
        f"{meses[mes_inicio]} 2026 - "
        f"{meses[mes_fin]} 2026"
    )