# from pomodule.base import Base
from pomodule.register import Register


class Login():
    """
    登录页面PO
    """
    def scan(self):
        """
        扫描二维码
        :return:
        """
        pass

    def goto_register(self):
        """
        点击“企业注册”，进入到注册页面PO
        :return:
        """
        self.driver.find_element_by_xpath('//*[@id="wework_admin.loginpage_wx_$"]/main/div[2]/a').click()
        return Register()



