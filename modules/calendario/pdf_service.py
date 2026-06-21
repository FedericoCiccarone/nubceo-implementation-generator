from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright
import os


def generar_pdf(
    cliente,
    semanas,
    tipo_integracion,
    periodo
):

    env = Environment(
        loader=FileSystemLoader("modules/calendario")
    )

    template = env.get_template("calendario.html")

    html = template.render(
        cliente=cliente,
        semanas=semanas,
        tipo_integracion=tipo_integracion,
        periodo=periodo

    )

    ruta_html = "output/calendario.html"
    ruta_pdf = (
    f"output/"
    f"Calendario Implementación - "
    f"{cliente} - {tipo_integracion}.pdf"
    )

    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html)


    with sync_playwright() as p:

        browser = p.chromium.launch()

        page = browser.new_page(
            viewport={
                "width": 1920,
                "height": 1080
            }
        )


        page.goto(
            "file://" + os.path.abspath(ruta_html)
        )


        page.pdf(
            path=ruta_pdf,
            width="1920px",
            height="1080px",
            print_background=True,
            margin={
                "top":"0",
                "right":"0",
                "bottom":"0",
                "left":"0"
            }
        )


        browser.close()


    return ruta_pdf