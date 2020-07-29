from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from test_wework.add_contact import AddContact


class Index:

    def __init__(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

    def goto_add_contact(self):

        self.driver.find_element_by_css_selector('.index_service_cnt_item').click()
        return AddContact(self.driver)