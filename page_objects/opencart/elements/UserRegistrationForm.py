import time

from selenium.webdriver.common.by import By
from page_object.opencart.BasePage import BasePage


class UserRegistrationForm(BasePage):
    INPUT_FIRST_NAME = (By.XPATH, "//input[@name='firstname']")
    INPUT_LAST_NAME = (By.XPATH, "//input[@name='lastname']")
    INPUT_EMAIL = (By.XPATH, "//input[@name='email']")
    INPUT_PHONE = (By.XPATH, "//input[@name='telephone']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name='password']")
    INPUT_PASSWORD_CONFIRM = (By.XPATH, "//input[@name='confirm']")

    CHECKBOX_PRIVACY_POLICY = (By.XPATH, "//input[@name='agree']")

    BTN_CONTINUE = (By.XPATH, "//input[@value='Continue']")

    SUCCESS_REGISTRATION_MESSAGE = (By.XPATH, "//h1[text()='Your Account Has Been Created!']")

    def fill_out_registration_form(self):
        _time = time.time_ns()
        self.browser.find_element(*self.INPUT_FIRST_NAME).send_keys(f"user{_time}")
        self.browser.find_element(*self.INPUT_LAST_NAME).send_keys(f"user{_time}")
        self.browser.find_element(*self.INPUT_EMAIL).send_keys(f"user{_time}@test.com")
        self.browser.find_element(*self.INPUT_PHONE).send_keys(f"{_time}")
        self.browser.find_element(*self.INPUT_PASSWORD).send_keys(f"qwerty")
        self.browser.find_element(*self.INPUT_PASSWORD_CONFIRM).send_keys(f"qwerty")
        return self

    def accept_privacy_policy(self):
        self.browser.find_element(*self.CHECKBOX_PRIVACY_POLICY).click()
        return self

    def send_registration_form(self):
        self.browser.find_element(*self.BTN_CONTINUE).click()
        return self

    def check_success_registration_message(self):
        self.browser.find_element(*self.SUCCESS_REGISTRATION_MESSAGE)
