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
        # sleep(3)

        def add_member_condition(x):
            element_len = len(self.finds(By.ID, 'username'))
            print(element_len)
            if element_len <= 0:
                print(f"未到找{element_len}")
                self.find(By.XPATH, '//*[@class="ww_operationBar"]//*[@class="qui_btn ww_btn js_add_member"]').click()
            else:
                print(f"找到了{element_len}")
                return element_len

        self.wait_for_condition(add_member_condition)

        return Contacts(self.driver)