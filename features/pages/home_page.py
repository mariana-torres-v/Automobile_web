import page

from .base_page import BasePage

URL = "https://www.bykon.com.mx/index.html"

class HomePage:

    def __init__(self):
        self.page = page

        self.header = page.get_by_text("Thriving in the new, the nowand the unknown.")
        self.btn_privacy_notice = page.get_by_role("link", name="Notice of Privacy")
        self.tab_services = page.get_by_role("link", name="Services ")
        self.submenu_digital = page.get_by_role("link", name="Digital")

    def navigate_to_home(self):
        self.page.goto(URL)

    def click_privacy_notice(self):
        self.btn_privacy_notice.click()

    def go_to_digital_services(self):
        self.tab_services.hover() # Hacemos hover si es un menú desplegable
        self.submenu_digital.click()