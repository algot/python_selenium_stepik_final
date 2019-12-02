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
        first_message = self.browser.find_element(*ProductPageLocators.FIRST_MESSAGE)
        assert f'×\n{product_name} has been added to your basket.' == first_message.text
        second_message = self.browser.find_element(*ProductPageLocators.SECOND_MESSAGE)
        assert 'Deferred benefit offer' in second_message.text
        total = self.browser.find_element(*ProductPageLocators.TOTAL).text
        assert total == self.get_price()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.TITLE).text

    def get_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text
