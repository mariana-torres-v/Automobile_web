from behave import given, then

from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.digital_page import DigitalPage


@given('que el usuario navega a la URL de "Digital-ByKon Consulting"')
def step_navigate_to_url(context):
    context.home_page = HomePage(context.page)

    context.home_page.navigate_to_home()


@then('la página principal se debe abrir y visualizar correctamente')
def step_verify_home_page_loads(context):
    # Validamos que el elemento 'header' esté visible en la pantalla
    expect(context.home_page.header).to_be_visible()

    # validamos que la URL sea la correcta
    expect(context.page).to_have_url("https://www.bykon.com.mx/index.html")

    # validamos el título de la pestaña del navegador
    expect(context.page).to_have_title("Bykon Home - ByKon Consulting")

