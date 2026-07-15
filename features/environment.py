import os
from playwright.sync_api import sync_playwright
from utils.report_helpers import adjuntar_captura_allure


def before_all(context):
    """
    Se ejecuta UNA sola vez. Aquí solo guardamos configuración,
    NO arrancamos Playwright todavía — eso pasa por escenario.
    """
    context.headless = os.environ.get("PLAYWRIGHT_HEADLESS", "true").lower() != "false"


def before_scenario(context, scenario):
    """
    Se ejecuta ANTES de CADA escenario.
    Ciclo de vida COMPLETO de Playwright por escenario:
    driver + browser + page. Esto es lo que espera browserstack-sdk
    para reportar cada escenario como una sesión independiente.
    """
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=context.headless)
    context.page = context.browser.new_page()


def after_step(context, step):
    # tomar screenshot si falla
    if step.status == "failed":
        if hasattr(context, "page") and context.page:
            nombre_error = f"FALLO: {step.name}"
            adjuntar_captura_allure(context.page, nombre_error)


def after_scenario(context, scenario):
    """
    Se ejecuta DESPUÉS de CADA escenario.
    Cerramos TODO lo que se creó en before_scenario, en orden inverso.
    """
    if getattr(context, "page", None):
        context.page.close()
    if getattr(context, "browser", None):
        context.browser.close()
    if getattr(context, "playwright", None):
        context.playwright.stop()


def after_all(context):
    """
    Ya no queda nada de Playwright que cerrar aquí —
    todo se cerró en after_scenario. Se deja por si en el futuro
    agregas algo que sí sea de alcance global (ej. cerrar un reporte).
    """
    pass