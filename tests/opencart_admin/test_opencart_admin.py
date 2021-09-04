from page_object.opencart_admin.LoginPageAdmin import LoginPageAdmin
from page_object.opencart_admin.MainPageAdmin import MainPageAdmin
from page_object.opencart_admin.ProductPageAdmin import ProductPageAdmin


def test_adding_a_new_product_in_the_admin_section(browser, user):
    LoginPageAdmin(browser).authorization_with(*user)
    MainPageAdmin(browser).go_to_product_page()
    ProductPageAdmin(browser).go_to_add_new_product_form()
    product_name = ProductPageAdmin(browser).create_new_product()
    ProductPageAdmin(browser).check_product_in_product_list(product_name)


def test_delete_product_in_the_admin_section(browser, user):
    LoginPageAdmin(browser).authorization_with(*user)
    MainPageAdmin(browser).go_to_product_page()
    ProductPageAdmin(browser) \
        .select_product_in_product_list_by_position(20) \
        .delete_product_in_product_list() \
        .check_alert_message()
