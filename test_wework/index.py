from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from test_wework.add_contact import AddContact
from test_wework.basepage import BasePage


class Index(BasePage):

    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_contact(self):
        self.driver.find_element_by_css_selector('.index_service_cnt_item').click()
        return AddContact(self.driver)