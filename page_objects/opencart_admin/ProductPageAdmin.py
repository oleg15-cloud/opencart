import random

from allure import step
from selenium.webdriver.common.by import By
from page_objects.opencart_admin.BasePageAdmin import BasePageAdmin
from page_objects.opencart_admin.elements.Alerts import Alerts
from page_objects.opencart_admin.elements.CreateProductForm import CreateProductFrom
from page_objects.opencart_admin.elements.SearchProductForm import SearchProductForm


class ProductPageAdmin(BasePageAdmin):
    BTN_ADD_NEW_PRODUCT = "//i[@class='fa fa-plus']"
    BTN_DELETE_PRODUCT = "//button[@data-original-title='Delete']"
    BTN_SAVE_PRODUCT = "//i[@class='fa fa-save']"

    INPUT_PRODUCT_NAME_FILTER = "//input[@name='filter_name']"

    CHECKBOXES = "//input[@type='checkbox']"

    ALERT_MESSAGE = "//div[@class='alert alert-success alert-dismissible']"

    @step("Open 'add new product' form")
    def go_to_add_new_product_form(self):
        self.logger.info("STEP: Click on 'add new product' button")
        self.get_element(self.BTN_ADD_NEW_PRODUCT).click()

    def create_new_product(self):
        product_name = f"Smartphone {random.randint(1, 1000)}"
        CreateProductFrom(self.browser) \
            .fill_out_product_form(product_name) \
            .save_product()
        return product_name

    def check_product_in_product_list(self, product_name):
        SearchProductForm(self.browser) \
            .fill_out_search_form(product_name) \
            .search() \
            .check_product_in_product_list(product_name)

    @step("Select product in checkbox")
    def select_product_in_product_list_by_position(self, position):
        self.logger.info(f"STEP: Select product in checkbox by position. checkbox_position: {position}")
        self.get_elements(self.CHECKBOXES)[position].click()
        return self

    @step("Click on 'delete product' button")
    def delete_product_in_product_list(self):
        self.logger.info("STEP: Delete product")
        self.get_element(self.BTN_DELETE_PRODUCT).click()
        Alerts(self.browser).alert_accept()
        return self

    @step("Check alert message")
    def check_alert_message(self):
        self.logger.info("STEP: Check alert message")
        self.get_element(self.ALERT_MESSAGE)
