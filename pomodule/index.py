from selenium import webdriver

# from pomodule.base import Base
from pomodule.login import Login
from pomodule.register import Register


class Index():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get('https://work.weixin.qq.com/')

    def goto_register(self):
        """
        点击“立即注册”，进入注册页面PO
        :return:
        """
        self.driver.find_element_by_xpath('//*[@id="tmp"]/div/a').click()
        return Register(self.driver)


    def goto_login(self):
        """
        点击“企业登录”， 进入登录页面PO
        :return:
        """

        self.driver.find_element_by_xpath('//*[@id="indexTop"]/div/aside/a[1]')
        return Login()