from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def text_basket_is_empty_is_displayed(self):
        expected_text = 'Your basket is empty.'
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        assert expected_text in empty_basket_message.text, f'"{expected_text}" is not displayed'

    def basket_is_empty(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket should be empty'
