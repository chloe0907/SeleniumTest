from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test_wework.basepage import BasePage


class AddContact(BasePage):

    def add_contact(self):
        self.find(By.ID, 'username').send_keys("小米")
        self.find(By.ID, 'memberAdd_acctid').send_keys('xiaomi')
        self.find(By.ID, 'memberAdd_phone').send_keys('18611221222')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

        return True
