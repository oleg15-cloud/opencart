from page_object.opencart_admin.BasePageAdmin import BasePageAdmin
from page_object.opencart_admin.elements.AuthFormAdmin import AuthFormAdmin


class LoginPageAdmin(BasePageAdmin):
    path = "/admin/"

    def authorization_with(self, username, password):
        self.browser.open(self.path)
        AuthFormAdmin(self.browser) \
            .fill_out_auth_form(username, password) \
            .send_auth_from()
