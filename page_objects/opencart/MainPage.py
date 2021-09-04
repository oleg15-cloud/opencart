from page_object.opencart.BasePage import BasePage
from page_object.opencart.elements.TopMenu import TopMenu


class MainPage(BasePage):

    def go_to_registration_page(self):
        TopMenu(self.browser).go_to_registration_page()

    def switch_to_another_currency(self):
        selected_currency = TopMenu(self.browser).switch_currency()
        return selected_currency

    def check_new_currency(self, selected_currency):
        TopMenu(self.browser).check_new_currency(selected_currency)
