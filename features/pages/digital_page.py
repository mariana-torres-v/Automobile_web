import page

class DigitalPage:

    def __init__(self):
        self.page = page

        self.header = page.get_by_role("paragraph").filter(has_text=re.compile(r"^Digital$"))
        self.btn_book_call = page.locator(".elementor-element.elementor-element-bd66d97 >"
                                             " .elementor-widget-container > .elementor-button-wrapper")
        self.header_book_call = page.get_by_text("Book a call")

    def click_book_a_call_btn(self):
        self.book_call_button.click()