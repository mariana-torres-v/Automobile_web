
class BookCallPage:

    def __init__(self, page):
        self.page = page

        self.header = self.page.get_by_text("Book a call").first