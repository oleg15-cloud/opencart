from allure import step
from page_objects.opencart_admin.BasePageAdmin import BasePageAdmin


class SearchProductForm(BasePageAdmin):
    INPUT_PRODUCT_NAME_FILTER = "//input[@name='filter_name']"

    BTN_FILTER = "//button[@id='button-filter']"

    @step("Fill out search form")
    def fill_out_search_form(self, product_name):
        self.logger.info(f"STEP: Fill out search form. product_name: {product_name}")
        self.get_element(self.INPUT_PRODUCT_NAME_FILTER).clear()
        self.get_element(self.INPUT_PRODUCT_NAME_FILTER).send_keys(product_name)
        return self

    @step("Click on 'filter' button")
    def search(self):
        self.logger.info("STEP: Click on 'search' button")
        self.get_element(self.BTN_FILTER).click()
        return self

    @step("Check product in product list")
    def check_product_in_product_list(self, product_name):
        self.logger.info(f"STEP: Check product in product list. product_name: {product_name}")
        self.get_element(f"//td[text()='{product_name}']")
