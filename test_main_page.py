from selenium.webdriver.remote import webdriver
from .pages.main_page import MainPage

link = 'http://selenium1py.pythonanywhere.com/'


def test_guest_can_go_to_login_page(browser: webdriver):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser: webdriver):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
