from page_object.opencart_admin.BasePageAdmin import BasePageAdmin
from page_object.opencart_admin.elements.Navigation import Navigation


class MainPageAdmin(BasePageAdmin):

    def go_to_product_page(self):
        Navigation(self.browser) \
            .open_catalog_dropdown() \
            .go_to_product_page()
