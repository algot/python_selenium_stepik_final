from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BUTTON_VIEW_BASKET = (By.CSS_SELECTOR, 'div.basket-mini a')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, 'div#content_inner>p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items .row')


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name = "login_submit"]')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[value="Register"]')


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div#messages>div:first-child')
    OFFER_MESSAGE = (By.CSS_SELECTOR, 'div#messages>div:nth-child(2)')
    BREADCRUMB_PRODUCT = (By.CSS_SELECTOR, 'ul.breadcrumb>li.active')
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button[value="Add to basket"]')
    TITLE = (By.CSS_SELECTOR, 'div.product_main>h1')
    TOTAL = (By.CSS_SELECTOR, 'div#messages>div.alert-info p>strong')
    PRICE = (By.CSS_SELECTOR, 'div.product_main>p.price_color')
