from time import sleep

from selenium import webdriver

# from pomodule.base import Base
from selenium.webdriver.android.webdriver import WebDriver


class Register():
    """
    企业注册PO
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        """
        输入内容，下拉框选择等
        :return:
        """
        self.driver.find_element_by_id('corp_name').send_keys('chloe1')
        sleep(3)
        return True
