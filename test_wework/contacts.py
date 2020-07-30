from time import sleep

from selenium.webdriver.common.by import By

from test_wework.add_contact import AddContact
from test_wework.basepage import BasePage


class Contacts(BasePage):
    def goto_addcontact(self):
        self.find(By.XPATH, '//*[@class="ww_operationBar"]//*[@class="qui_btn ww_btn js_add_member"]').click()
        # self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        return AddContact(self.driver)