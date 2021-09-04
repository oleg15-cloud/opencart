import random

from selenium.webdriver.common.by import By
from page_object.opencart_admin.BasePageAdmin import BasePageAdmin
from page_object.opencart_admin.elements.Alerts import Alerts
from page_object.opencart_admin.elements.CreateProductForm import CreateProductFrom
from page_object.opencart_admin.elements.SearchProductForm import SearchProductForm


class ProductPageAdmin(BasePageAdmin):
    BTN_ADD_NEW_PRODUCT = (By.XPATH, "//i[@class='fa fa-plus']")
    BTN_DELETE_PRODUCT = (By.XPATH, "//button[@data-original-title='Delete']")
    BTN_SAVE_PRODUCT = (By.XPATH, "//i[@class='fa fa-save']")

    INPUT_PRODUCT_NAME_FILTER = (By.XPATH, "//input[@name='filter_name']")

    CHECKBOXES = (By.XPATH, "//input[@type='checkbox']")

    ALERT_MESSAGE = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def go_to_add_new_product_form(self):
        self.browser.find_element(*self.BTN_ADD_NEW_PRODUCT).click()

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

    def select_product_in_product_list_by_position(self, position):
        self.browser.find_elements(*self.CHECKBOXES)[position].click()
        return self

    def delete_product_in_product_list(self):
        self.browser.find_element(*self.BTN_DELETE_PRODUCT).click()
        Alerts(self.browser).alert_accept()
        return self

    def check_alert_message(self):
        self.browser.find_element(*self.ALERT_MESSAGE)
