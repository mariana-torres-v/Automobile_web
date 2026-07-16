import os
from playwright.sync_api import sync_playwright
from utils.report_helpers import adjuntar_captura_allure


def before_all(context):
    """
    Se ejecuta UNA sola vez. Aquí solo guardamos configuración,
    NO arrancamos Playwright todavía — eso pasa por escenario.
    """
    context.headless = False
    #context.headless = os.environ.get("PLAYWRIGHT_HEADLESS", "true").lower() != "false"

def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=context.headless
    )
    context.context = context.browser.new_context(
        viewport={"width": 1920, "height": 1080}
    )
    context.page = context.context.new_page()


def after_step(context, step):
    # tomar screenshot si falla
    if step.status == "failed":
        if hasattr(context, "page") and context.page:
            nombre_error = f"FALLO: {step.name}"
            adjuntar_captura_allure(context.page, nombre_error)


def after_scenario(context, scenario):
    """
    Se ejecuta DESPUÉS de CADA escenario.
    Cerramos TO'DO lo que se creó en before_scenario, en orden inverso.
    """
    if getattr(context, "page", None):
        context.page.close()
    if getattr(context, "context", None):  # Cerramos el contexto explícitamente
        context.context.close()
    if getattr(context, "browser", None):
        context.browser.close()
    if getattr(context, "playwright", None):
        context.playwright.stop()


def after_all(context):
    pass