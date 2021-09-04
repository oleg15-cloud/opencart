from selenium.webdriver.common.by import By
from page_objects.opencart_admin.BasePageAdmin import BasePageAdmin


class SearchProductForm(BasePageAdmin):
    INPUT_PRODUCT_NAME_FILTER = (By.XPATH, "//input[@name='filter_name']")

    BTN_FILTER = (By.XPATH, "//button[@id='button-filter']")

    def fill_out_search_form(self, product_name):
        self.logger.info("Fill out search form")
        self.browser.find_element(*self.INPUT_PRODUCT_NAME_FILTER).clear()
        self.browser.find_element(*self.INPUT_PRODUCT_NAME_FILTER).send_keys(product_name)
        return self

    def search(self):
        self.logger.info("Click search")
        self.browser.find_element(*self.BTN_FILTER).click()
        return self

    def check_product_in_product_list(self, product_name):
        self.logger.info("Check product in product list")
        self.browser.find_element(By.XPATH, f"//td[text()='{product_name}']")
