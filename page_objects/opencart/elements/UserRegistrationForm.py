import time

from allure import step
from page_objects.opencart.BasePage import BasePage


class UserRegistrationForm(BasePage):
    INPUT_FIRST_NAME = "//input[@name='firstname']"
    INPUT_LAST_NAME = "//input[@name='lastname']"
    INPUT_EMAIL = "//input[@name='email']"
    INPUT_PHONE = "//input[@name='telephone']"
    INPUT_PASSWORD = "//input[@name='password']"
    INPUT_PASSWORD_CONFIRM = "//input[@name='confirm']"

    CHECKBOX_PRIVACY_POLICY = "//input[@name='agree']"

    BTN_CONTINUE = "//input[@value='Continue']"

    SUCCESS_REGISTRATION_MESSAGE = "//h1[text()='Your Account Has Been Created!']"

    @step("Fill out registration form")
    def fill_out_registration_form(self):
        _time = time.time_ns()
        self.logger.info(f"STEP: Fill out registration form: email: user{_time}@test.com, password: qwerty")
        self.get_element(self.INPUT_FIRST_NAME).send_keys(f"user{_time}")
        self.get_element(self.INPUT_LAST_NAME).send_keys(f"user{_time}")
        self.get_element(self.INPUT_EMAIL).send_keys(f"user{_time}@test.com")
        self.get_element(self.INPUT_PHONE).send_keys(f"{_time}")
        self.get_element(self.INPUT_PASSWORD).send_keys(f"qwerty")
        self.get_element(self.INPUT_PASSWORD_CONFIRM).send_keys(f"qwerty")
        return self

    @step("Accept privacy policy")
    def accept_privacy_policy(self):
        self.logger.info("STEP: Accept privacy policy")
        self.get_element(self.CHECKBOX_PRIVACY_POLICY).click()
        return self

    @step("Submit registration form")
    def send_registration_form(self):
        self.logger.info("STEP: Submit registration form")
        self.get_element(self.BTN_CONTINUE).click()
        return self

    @step("Check success registration message after submit form")
    def check_success_registration_message(self):
        self.logger.info("STEP: Check success registration message")
        self.get_element(self.SUCCESS_REGISTRATION_MESSAGE)
