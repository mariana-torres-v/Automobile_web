import os
from playwright.sync_api import sync_playwright
from utils.report_helpers import adjuntar_captura_allure


def before_all(context):
    #headless = os.environ.get("PLAYWRIGHT_HEADLESS", "true").lower() != "false"
    context.headless = os.environ.get("PLAYWRIGHT_HEADLESS", "false").lower() == "true"
    context.playwright = sync_playwright().start()

    context.browser = context.playwright.chromium.launch(headless=context.headless)
    #context.browser = context.playwright.firefox.launch(headless=context.headless)

    context.page = context.browser.new_page()

def after_step(context, step):
    # tomar screenshot si falla
    if step.status == "failed":
        if hasattr(context, "page") and context.page:
            nombre_error = f"FALLO: {step.name}"
            adjuntar_captura_allure(context.page, nombre_error)

def after_all(context):
    if getattr(context, "page", None):
        context.page.close()
    if getattr(context, "browser", None):
        context.browser.close()
    if getattr(context, "playwright", None):
        context.playwright.stop()
