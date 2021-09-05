import logging
import allure

from selenium import common
from selenium.webdriver.common.by import By


class BasePageAdmin:

    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)

    def get_element(self, locator):
        try:
            return self.browser.find_element(By.XPATH, locator)
        except common.exceptions.NoSuchElementException:
            self.logger.error(f"Element '{locator}' not found on page!")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element '{locator}' not found on page!")

    def get_elements(self, locator):
        try:
            return self.browser.find_elements(By.XPATH, locator)
        except common.exceptions.NoSuchElementException:
            self.logger.error(f"Elements '{locator}' not found on page!")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Elements '{locator}' not found on page!")
