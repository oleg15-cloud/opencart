from selenium.webdriver.common.by import By
from page_objects.opencart_admin.BasePageAdmin import BasePageAdmin


class AuthFormAdmin(BasePageAdmin):
    path = "/admin/"

    INPUT_USERNAME = (By.XPATH, "//input[@name='username']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name='password']")
    BTN_LOGIN = (By.XPATH, "//button[@class='btn btn-primary']")

    def fill_out_auth_form(self, username, password):
        self.logger.info("Fill out auth form")
        self.browser.find_element(*self.INPUT_USERNAME).clear()
        self.browser.find_element(*self.INPUT_USERNAME).send_keys(username)
        self.browser.find_element(*self.INPUT_PASSWORD).clear()
        self.browser.find_element(*self.INPUT_PASSWORD).send_keys(password)
        return self

    def send_auth_from(self):
        self.logger.info("Submit auth form")
        self.browser.find_element(*self.BTN_LOGIN).click()
