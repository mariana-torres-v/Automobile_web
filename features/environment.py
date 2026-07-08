import os
from playwright.sync_api import sync_playwright


def before_all(context):
    headless = os.environ.get("PLAYWRIGHT_HEADLESS", "true").lower() != "false"
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=headless)
    context.page = context.browser.new_page()


def after_all(context):
    if getattr(context, "page", None):
        context.page.close()
    if getattr(context, "browser", None):
        context.browser.close()
    if getattr(context, "playwright", None):
        context.playwright.stop()
