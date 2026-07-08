from .base_page import BasePage


class HomePage(BasePage):
    URL = "https://www.bykon.com.mx/index.html"

    def open(self):
        self.goto(self.URL)

    def get_title(self) -> str:
        return self.title()
