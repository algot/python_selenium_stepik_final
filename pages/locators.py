from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name = "login_submit"]')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[value="Register"]')


class ProductPageLocators:
    FIRST_MESSAGE = (By.CSS_SELECTOR, 'div#messages>div:first-child')
    SECOND_MESSAGE = (By.CSS_SELECTOR, 'div#messages>div:nth-child(2)')
    BREADCRUMB_PRODUCT = (By.CSS_SELECTOR, 'ul.breadcrumb>li.active')
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button[value="Add to basket"]')
    TOTAL = (By.CSS_SELECTOR, 'div#messages>div.alert-info p>strong')
    PRICE = (By.CSS_SELECTOR, 'div.product_main>p.price_color')
