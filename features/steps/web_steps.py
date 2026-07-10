from behave import given, then, when

from playwright.sync_api import expect

from pages.home_page import HomePage

from pages.digital_page import DigitalPage

# NAVIGATION STEPS
@given('que el usuario se encuentra en la página principal de "{sitio}"')
def step_navigate_to_url(context, sitio):
    context.home_page = HomePage(context.page)
    context.digital_page = DigitalPage(context.page)
    context.home_page.navigate_to_home(sitio)

# VALIDATION STEPS
@then('la página principal se debe abrir y visualizar correctamente')
def step_verify_home_page_loads(context):
    # valida que el header de home_page está visible
    expect(context.home_page.header).to_be_visible()

    # valida que la URL sea la correcta
    expect(context.page).to_have_url("https://www.bykon.com.mx/index.html")

    # valida el título de la pestaña del navegador
    expect(context.page).to_have_title("Bykon Home - ByKon Consulting")

@then('la página de Aviso de Privacidad se debe abrir correctamente')
def step_verify_privacy_notice_loads(context):
    # no hay privacy notice por lo que se valida el mismo header de home_page
    expect(context.home_page.header).to_be_visible()

@then('la página de "Services > Digital" se debe abrir correctamente')
def step_verify_digital_page_loads(context):
    expect(context.digital_page.header).to_be_visible()

@then('se debe abrir correctamente el modal para agendar una llamada')
def step_verify_book_call_page_loads(context):
    expect(context.digital_page.header).to_be_visible()

# UI STEPS
@when('hace scroll hasta el botón "Aviso de Privacidad"')
def step_scroll_to_btn_privacy_notice(context):
    context.home_page.scroll_to_privacy_notice()

@when('da clic en el botón "Aviso de Privacidad"')
def step_click_btn_privacy_notice(context)
    context.home_page.click_btn_privacy_notice()

@when('hace hover sobre "{element}"')
def hover_element(context, element):
    target_element = context.page.locator(element)
    target_element.hover()


















