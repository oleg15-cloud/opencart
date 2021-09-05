from allure import step
from page_objects.opencart_admin.BasePageAdmin import BasePageAdmin


class AuthFormAdmin(BasePageAdmin):
    path = "/admin/"

    INPUT_USERNAME = "//input[@name='username']"
    INPUT_PASSWORD = "//input[@name='password']"
    BTN_LOGIN = "//button[@class='btn btn-primary']"

    @step("Fill out authorization form")
    def fill_out_auth_form(self, username, password):
        self.logger.info(f"STEP: Fill out authorization form. username: {username}, password: {password}")
        self.get_element(self.INPUT_USERNAME).clear()
        self.get_element(self.INPUT_USERNAME).send_keys(username)
        self.get_element(self.INPUT_PASSWORD).clear()
        self.get_element(self.INPUT_PASSWORD).send_keys(password)
        return self

    @step("Submit authorization form")
    def send_auth_from(self):
        self.logger.info("STEP: Submit authorization form")
        self.get_element(self.BTN_LOGIN).click()
