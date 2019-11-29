from selenium.webdriver import Remote

link = 'http://selenium1py.pythonanywhere.com/'


def test_guest_can_go_to_login_page(browser: Remote):
    browser.get(link)
    go_to_login_page(browser)

