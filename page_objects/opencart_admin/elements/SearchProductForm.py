from allure import step
from selenium.webdriver.common.by import By
from page_objects.opencart_admin.BasePageAdmin import BasePageAdmin


class SearchProductForm(BasePageAdmin):
    INPUT_PRODUCT_NAME_FILTER = (By.XPATH, "//input[@name='filter_name']")

    BTN_FILTER = (By.XPATH, "//button[@id='button-filter']")

    @step("Fill out search form")
    def fill_out_search_form(self, product_name):
        self.logger.info(f"STEP: Fill out search form. product_name: {product_name}")
        self.browser.find_element(*self.INPUT_PRODUCT_NAME_FILTER).clear()
        self.browser.find_element(*self.INPUT_PRODUCT_NAME_FILTER).send_keys(product_name)
        return self

    @step("Click on 'filter' button")
    def search(self):
        self.logger.info("STEP: Click on 'search' button")
        self.browser.find_element(*self.BTN_FILTER).click()
        return self

    @step("Check product in product list")
    def check_product_in_product_list(self, product_name):
        self.logger.info(f"STEP: Check product in product list. product_name: {product_name}")
        self.browser.find_element(By.XPATH, f"//td[text()='{product_name}']")
