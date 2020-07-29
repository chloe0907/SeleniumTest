from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BasePage:

    _base_url = ''

    def __init__(self, driver=None):
        if driver is None:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)

            self.driver.maximize_window()
            self.driver.implicitly_wait(3)
        else:
            self.driver = driver

        if self._base_url != "":
            self.driver.get(self._base_url)