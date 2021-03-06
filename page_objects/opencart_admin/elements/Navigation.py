from allure import step
from selenium.webdriver.common.by import By
from page_objects.opencart_admin.BasePageAdmin import BasePageAdmin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Navigation(BasePageAdmin):
    NAVIGATION_CATALOG = "//li[@id='menu-catalog']"
    NAVIGATION_CATALOG_PRODUCTS = "//a[text()='Products']"

    @step("Open dropdown 'Catalog'")
    def open_catalog_dropdown(self):
        self.logger.info("STEP: Open catalog dropdown")
        self.get_element(self.NAVIGATION_CATALOG).click()
        return self

    @step("Open product page")
    def go_to_product_page(self):
        self.logger.info("STEP: Go to product page")
        WebDriverWait(self.browser, 3).until(
            ec.visibility_of_element_located((By.XPATH, self.NAVIGATION_CATALOG_PRODUCTS))).click()
