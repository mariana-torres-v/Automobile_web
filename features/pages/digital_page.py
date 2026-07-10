import re

class DigitalPage:

    def __init__(self, page):
        self.page = page

        self.header = self.page.get_by_role("paragraph").filter(has_text=re.compile(r"^Digital$"))
        self.btn_book_call = self.page.locator(".elementor-element.elementor-element-bd66d97 >"
                                             " .elementor-widget-container > .elementor-button-wrapper")
        self.header_es =self.page.get_by_text("Nuestros servicios")

    def click_btn_book_a_call(self):
        self.btn_book_call.first.click()


