from allure import title
from page_objects.opencart.MainPage import MainPage
from page_objects.opencart.RegistrationPage import RegistrationPage


@title("Registration new user")
def test_registration_new_user(browser):
    MainPage(browser).go_to_registration_page()
    RegistrationPage(browser) \
        .create_new_user() \
        .check_success_registration_message()


@title("Switch to another currency")
def test_switch_currency(browser):
    currency = MainPage(browser).switch_to_another_currency()
    MainPage(browser).check_new_currency(currency)
