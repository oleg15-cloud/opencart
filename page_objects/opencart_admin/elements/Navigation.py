from selenium.webdriver.common.by import By
from page_object.opencart_admin.BasePageAdmin import BasePageAdmin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Navigation(BasePageAdmin):
    NAVIGATION_CATALOG = (By.XPATH, "//li[@id='menu-catalog']")
    NAVIGATION_CATALOG_PRODUCTS = "//a[text()='Products']"

    def open_catalog_dropdown(self):
        self.browser.find_element(*self.NAVIGATION_CATALOG).click()
        return self

    def go_to_product_page(self):
        WebDriverWait(self.browser, 3).until(
            ec.visibility_of_element_located((By.XPATH, self.NAVIGATION_CATALOG_PRODUCTS))).click()
