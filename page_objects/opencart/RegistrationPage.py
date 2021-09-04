from page_object.opencart.elements.UserRegistrationForm import UserRegistrationForm
from page_object.opencart.BasePage import BasePage


class RegistrationPage(BasePage):

    def create_new_user(self):
        UserRegistrationForm(self.browser) \
            .fill_out_registration_form() \
            .accept_privacy_policy() \
            .send_registration_form()
        return self

    def check_success_registration_message(self):
        UserRegistrationForm(self.browser).check_success_registration_message()
