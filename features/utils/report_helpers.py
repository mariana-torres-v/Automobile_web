import allure
from allure_commons.types import AttachmentType


def adjuntar_captura_allure(page, nombre_captura, mensaje=None):
    """
    Toma una captura de pantalla a página completa con Playwright
    y la adjunta directamente al reporte de Allure sin guardar archivos locales.
    """
    try:
        screenshot_bytes = page.screenshot(full_page=True)
        allure.attach(
            body=screenshot_bytes,
            name=nombre_captura,
            attachment_type=AttachmentType.PNG
        )

        if mensaje:
            allure.attach(
                body=mensaje,
                name="Detalle de Validación",
                attachment_type=AttachmentType.TEXT
            )

    except Exception as e:
        print(f"⚠️ No se pudo adjuntar la captura a Allure: {e}")