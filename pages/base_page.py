from selenium.webdriver import Remote


class BasePage:

    def __init__(self, browser, url):
        self.browser: Remote = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
