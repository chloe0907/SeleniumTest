from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_wework.add_contact import AddContact
from test_wework.basepage import BasePage
from test_wework.contacts import Contacts


class Index(BasePage):

    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_contact(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_item').click()
        return AddContact(self.driver)

    def goto_contacts(self):
        self.find(By.ID, 'menu_contacts').click()
        # 添加成员按钮出来了，但是添加功能的逻辑还没出来，所以，点击了没有反应。等待一会儿，等待添加功能的逻辑出来了，再次点击添加成员，就生效了。
        sleep(3)
        return Contacts(self.driver)