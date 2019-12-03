from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, '"login" is absent in URL'

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        assert self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        assert self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)

    def register_new_user(self, email, password):
        registration_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        registration_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        registration_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)

        registration_email.send_keys(email)
        registration_password.send_keys(password)
        registration_password_confirm.send_keys(password)
        registration_button.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), 'user is not logged in'
