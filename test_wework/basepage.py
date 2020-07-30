from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    driver = None
    _base_url = ''

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
            print(f"1111111111=========={driver}")
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)
        else:
            self.driver = driver
            print(f"222222222=========={driver}")
            print(f"333333333=========={BasePage.driver}")

        if self._base_url != "":
            self.driver.get(self._base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def wait_for_condition(self, condition):
        print(f"webdriver wait -------{condition}")
        WebDriverWait(self.driver, 10).until(condition)
        print("=====================webdriver end")
