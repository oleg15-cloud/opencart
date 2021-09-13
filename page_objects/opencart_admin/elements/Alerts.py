from allure import step
from page_objects.opencart_admin.BasePageAdmin import BasePageAdmin


class Alerts(BasePageAdmin):

    @step("Accept alert on page")
    def alert_accept(self):
        self.logger.info("STEP: Accept alert on page")
        self.browser.switch_to.alert.accept()
