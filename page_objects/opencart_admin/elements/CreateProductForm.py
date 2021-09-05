from allure import step
from selenium.webdriver.common.by import By
from page_objects.opencart_admin.BasePageAdmin import BasePageAdmin


class CreateProductFrom(BasePageAdmin):
    INPUT_PRODUCT_NAME = (By.XPATH, "//input[@id='input-name1']")
    INPUT_META_TAG_TITLE = (By.XPATH, "//input[@id='input-meta-title1']")
    INPUT_MODEL = (By.XPATH, "//input[@id='input-model']")

    DATA_SECTION = (By.XPATH, "//a[text()='Data']")

    BTN_SAVE_PRODUCT = (By.XPATH, "//i[@class='fa fa-save']")

    @step("Fill out product form")
    def fill_out_product_form(self, product_name):
        self.logger.info(f"STEP: Fill out product form. product_name: {product_name}, "
                         f"meta_tag_title: {product_name}, "
                         f"model: {product_name}")
        self.browser.find_element(*self.INPUT_PRODUCT_NAME).clear()
        self.browser.find_element(*self.INPUT_PRODUCT_NAME).send_keys(product_name)
        self.browser.find_element(*self.INPUT_META_TAG_TITLE).clear()
        self.browser.find_element(*self.INPUT_META_TAG_TITLE).send_keys(product_name)
        self.browser.find_element(*self.DATA_SECTION).click()
        self.browser.find_element(*self.INPUT_MODEL).clear()
        self.browser.find_element(*self.INPUT_MODEL).send_keys(product_name)
        return self

    @step("Save new product")
    def save_product(self):
        self.logger.info("STEP: Save product form")
        self.browser.find_element(*self.BTN_SAVE_PRODUCT).click()
