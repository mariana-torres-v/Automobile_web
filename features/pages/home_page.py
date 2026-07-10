from .base_page import BasePage


URL = "https://www.bykon.com.mx/index.html"


class HomePage:

    def __init__(self, page):
        self.page = page

        self.header = self.page.get_by_text("Thriving in the new, the nowand the unknown.")
        self.btn_privacy_notice = self.page.get_by_role("link", name="Notice of Privacy")
        self.tab_services = self.page.get_by_role("link", name="Services ")
        self.submenu_digital = self.page.get_by_role("link", name="Digital")
        self.btn_mexico_flag = self.page.get_by_role("link", name="es_MX")

    def navigate_to_home(self):
        self.page.goto(URL)

    def scroll_to_btn_privacy_notice(self):
        self.btn_privacy_notice.scroll_into_view_if_needed()

    def click_btn_privacy_notice(self):
        self.btn_privacy_notice.click()

    def navigate_to_digital_services(self):
        self.tab_services.hover() # Hacemos hover al menú desplegable
        self.submenu_digital.click()

    def go_to_page_translated_by_google(self):
        current_url = self.page.url
        google_translate_url = f"https://translate.google.com/translate?sl=en&tl=es&u={current_url}"
        self.page.goto(google_translate_url)
        self.page.wait_for_load_state("networkidle")

    def click_mexico_flag(self):
        self.btn_mexico_flag.click()