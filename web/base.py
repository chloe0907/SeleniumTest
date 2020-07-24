import os

from selenium import webdriver


class Base:
    def setup(self):
        browser = os.getenv('browser')
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            opt = webdriver.ChromeOptions()
            opt.add_experimental_option('w3c', False)
            self.driver = webdriver.Chrome(chrome_options=opt)

        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()