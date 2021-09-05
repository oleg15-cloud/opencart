import random

from allure import step
from selenium.webdriver.common.by import By
from page_objects.opencart.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TopMenu(BasePage):
    BTN_MY_ACCOUNT = (By.XPATH, "//i[@class='fa fa-user']")
    BTN_MY_ACCOUNT_REGISTER = (By.XPATH, "//a[text()='Register']")
    BTN_CURRENCY = "//button[@class='btn btn-link dropdown-toggle']"

    CURRENCIES = (By.XPATH, "//li/button")
    CURRENCY_STRONG = (By.XPATH, "//strong")

    @step("Go to registration page through 'my_account'")
    def go_to_registration_page(self):
        self.logger.info("STEP: Go to registration page")
        self.browser.find_element(*self.BTN_MY_ACCOUNT).click()
        self.browser.find_element(*self.BTN_MY_ACCOUNT_REGISTER).click()

    @step("Switch to random another currency through Top Menu")
    def switch_currency(self):
        self.logger.info("STEP: Switch currency")
        WebDriverWait(self.browser, 2).until(ec.visibility_of_element_located((By.XPATH, self.BTN_CURRENCY))).click()
        currencies = self.browser.find_elements(*self.CURRENCIES)
        random_currency = random.randint(0, len(currencies) - 1)
        currencies[random_currency].click()
        return self.browser.find_element(*self.CURRENCY_STRONG)

    @step("Check new currency at Top Menu")
    def check_new_currency(self, web_element):
        self.logger.info("STEP: Check new currency")
        assert web_element == self.browser.find_element(*self.CURRENCY_STRONG)
