from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def assert_product_added(self):
        product_name = self.get_product_name()
        breadcrumb_product = self.browser.find_element(*ProductPageLocators.BREADCRUMB_PRODUCT)
        assert breadcrumb_product.text == product_name
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert f'×\n{product_name} has been added to your basket.' == success_message.text
        offer_message = self.browser.find_element(*ProductPageLocators.OFFER_MESSAGE)
        assert 'Deferred benefit offer' in offer_message.text
        total = self.browser.find_element(*ProductPageLocators.TOTAL).text
        assert total == self.get_price()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.TITLE).text

    def get_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message should not disappear"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should disappear"
