from selenium.webdriver.common.by import By
from page_object.opencart_admin.BasePageAdmin import BasePageAdmin


class CreateProductFrom(BasePageAdmin):
    INPUT_PRODUCT_NAME = (By.XPATH, "//input[@id='input-name1']")
    INPUT_META_TAG_TITLE = (By.XPATH, "//input[@id='input-meta-title1']")
    INPUT_MODEL = (By.XPATH, "//input[@id='input-model']")

    DATA_SECTION = (By.XPATH, "//a[text()='Data']")

    BTN_SAVE_PRODUCT = (By.XPATH, "//i[@class='fa fa-save']")

    def fill_out_product_form(self, product_name):
        self.browser.find_element(*self.INPUT_PRODUCT_NAME).clear()
        self.browser.find_element(*self.INPUT_PRODUCT_NAME).send_keys(product_name)
        self.browser.find_element(*self.INPUT_META_TAG_TITLE).clear()
        self.browser.find_element(*self.INPUT_META_TAG_TITLE).send_keys(product_name)
        self.browser.find_element(*self.DATA_SECTION).click()
        self.browser.find_element(*self.INPUT_MODEL).clear()
        self.browser.find_element(*self.INPUT_MODEL).send_keys(product_name)
        return self

    def save_product(self):
        self.browser.find_element(*self.BTN_SAVE_PRODUCT).click()
