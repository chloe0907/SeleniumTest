from selenium.webdriver.android.webdriver import WebDriver


class AddContact:

    def __init__(self, driver:WebDriver):
        self.driver = driver

    def add_contact(self):
        self.driver.find_element_by_id('username').send_keys("小米")
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('xiaomi')
        self.driver.find_element_by_id('memberAdd_phone').send_keys('18611221222')
        self.driver.find_element_by_css_selector('.js_btn_continue').click()

        return True
