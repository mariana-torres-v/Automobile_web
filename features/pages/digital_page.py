import page

class DigitalPage:

    def __init__(self):
        self.page = page

        self.header = page.get_by_role("paragraph").filter(has_text=re.compile(r"^Digital$"))
        self.book_call_button = page.locator(".elementor-element.elementor-element-bd66d97 >"
                                             " .elementor-widget-container > .elementor-button-wrapper")

    def click_book_a_call_btn(self):
        self.book_call_button.click()