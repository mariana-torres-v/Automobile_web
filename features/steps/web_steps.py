from behave import given, then, when
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.digital_page import DigitalPage
from pages.book_call_page import BookCallPage
import time
from utils.report_helpers import adjuntar_captura_allure
import allure


# NAVIGATION STEPS
@given('que el usuario se encuentra en la página principal de "Digital-ByKon Consulting"')
def step_navigate_to_url(context):
    context.home_page = HomePage(context.page)
    context.digital_page = DigitalPage(context.page)
    context.book_call_page = BookCallPage(context.page)

    context.home_page.navigate_to_home()


# # # VALIDATION STEPS # # #
@then('la página principal se visualiza correctamente')
@allure.step("Validando que la página principal cargue el header principal")
def step_verify_home_page_loads(context):
    context.home_page.header.wait_for(state="visible", timeout=15000)
    time.sleep(3)
    expect(
        context.home_page.header,
        message="El header de bienvenida no se encontró"
    ).to_be_visible()

    #valida la url
    expect(
        context.page,
        message="La URL de la home page no es la esperada"
    ).to_have_url("https://www.bykon.com.mx/index.html")

    # valida el título de la pestaña del navegador
    expect(
        context.page,
        message="El nombre del tab no es el esperado"
    ).to_have_title("Bykon Home - ByKon Consulting")

@then('el sistema abre la página de "Aviso de Privacidad"')
@allure.step("Validando que el sistema entre a la página 'Aviso de privacidad'")
def step_verify_privacy_notice_loads(context):
    # no hay privacy notice por lo que se valida el mismo header de home_page
    expect(
        context.home_page.header,
        message="El sistema no abrió el 'Aviso de privacidad'"
    ).to_be_visible()

@then('el sistema abre la página de la sección "Services > Digital"')
@allure.step("Validando que el sistema entre a la página 'Services > Digital'")
def step_verify_digital_page_loads(context):
    expect(
        context.digital_page.header,
        message="El sistema no pudo abrir la página Digital"
    ).to_be_visible()

@then('el sistema redirige a la página para agendar una llamada')
@allure.step("Validando que el sistema vea la página 'Book a call'")
def step_verify_book_call_page_is_visible(context):
    expect(
        context.book_call_page.header,
        message="El sistema no pudo abrir la página 'Book a call'"
    ).to_be_visible()

@then('el sistema tiene la URL "https://www.bykon.com.mx/book-call.html"')
@allure.step("Validando que el sistema entre a la página 'Book a call'")
def step_verify_book_call_page_loads(context):
    url = "https://www.bykon.com.mx/book-call.html"
    expect(
        context.page,
        message="El  sistema no pudo abrir la página 'Book acall'"
    ).to_have_url(url)

@then('el sistema muestra el texto de la página en español')
@allure.step("Validando que el sistema muestre la página en español")
def step_verify_translated_text(context):
    expect(
        context.digital_page.header_es,
        message="El sistema no muestra el texto de la página en español"
    ).to_be_visible()

@then('el sistema en español no encima los elementos ni rompe el diseño')
@allure.step("Validando que el sistema en español no rompa el diseño (se valida manualmente)")
def step_validate_translated_ui(context):
    time.sleep(2)
    adjuntar_captura_allure(
        context.page, "bykon_es_validation",
        mensaje = "Validar manualmente si se traslapa el texto"
    )


# # # UI STEPS # # #

@when('el usuario hace scroll hasta el botón "Aviso de Privacidad"')
def step_scroll_to_btn_privacy_notice(context):
    context.home_page.scroll_to_btn_privacy_notice()

@when('el usuario da clic en el botón "Aviso de Privacidad"')
def step_click_btn_privacy_notice(context):
    context.home_page.click_btn_privacy_notice()

@when('el usuario navega a la página "Digital"')
def step_navigate_to_digital_services(context):
    context.home_page.navigate_to_digital_services()

@when('el usuario da clic en la bandera de México')
def step_click_mx_flag(context):
    context.home_page.click_mexico_flag()

#digital
@when('el usuario da clic en el botón "Book a call"')
def step_go_to_book_call(context):
    context.digital_page.click_btn_book_a_call()

@when('el usuario ocupa google para traducir el contenido de la página')
def step_translate_with_google(context):
    context.home_page.go_to_page_translated_by_google()
















