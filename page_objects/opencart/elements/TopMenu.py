import random

from selenium.webdriver.common.by import By
from page_object.opencart.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TopMenu(BasePage):
    BTN_MY_ACCOUNT = (By.XPATH, "//i[@class='fa fa-user']")
    BTN_MY_ACCOUNT_REGISTER = (By.XPATH, "//a[text()='Register']")
    BTN_CURRENCY = "//button[@class='btn btn-link dropdown-toggle']"

    CURRENCIES = (By.XPATH, "//li/button")
    CURRENCY_STRONG = (By.XPATH, "//strong")

    def go_to_registration_page(self):
        self.browser.find_element(*self.BTN_MY_ACCOUNT).click()
        self.browser.find_element(*self.BTN_MY_ACCOUNT_REGISTER).click()

    def switch_currency(self):
        WebDriverWait(self.browser, 2).until(ec.visibility_of_element_located((By.XPATH, self.BTN_CURRENCY))).click()
        currencies = self.browser.find_elements(*self.CURRENCIES)
        random_currency = random.randint(0, len(currencies) - 1)
        currencies[random_currency].click()
        return self.browser.find_element(*self.CURRENCY_STRONG)

    def check_new_currency(self, web_element):
        assert web_element == self.browser.find_element(*self.CURRENCY_STRONG)
