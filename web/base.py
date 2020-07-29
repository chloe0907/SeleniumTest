import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Base:
    def setup(self):
        browser = os.getenv('browser')
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            # opt = webdriver.ChromeOptions()
            # opt.add_experimental_option('w3c', False)

            # 用浏览器打开调试端口进行通信
            # 浏览器要使用 --remote-debugging-port=9222开启调试

            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()