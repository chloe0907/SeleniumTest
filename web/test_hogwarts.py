import os
import shelve
from time import sleep

import pytest
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from web.base import Base


class TestHogwarts(Base):

    @pytest.mark.skip
    def test_hogwarts(self):

        self.driver.get("https://testerhome.com/")
        # def wait(x):
        #     return x.find_element_by_link_text('社团')
        # WebDriverWait(self.driver, 10).until(wait)
        WebDriverWait(self.driver, 10).until(lambda x:x.find_element_by_link_text("社团123"))
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("霍格沃兹测试学院").click()
        sleep(1)
        # self.driver.find_element_by_xpath('//*[@class="topic media topic-24415"]').click()

    @pytest.mark.skip
    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        # self.driver.find_element(By.ID, 'kw').send_keys("appium")
        # self.driver.find_element(By.XPATH, "//*[@id='kw']").send_keys("appium")
        # self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("appium")
        self.driver.find_element(By.NAME, 'wd').send_keys("appium")

    @pytest.mark.skip
    def test_actionchains(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        # ele_click =self.driver.find_element_by_xpath('/html/body/form/input[2]')
        ele_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        ele_double_click = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        ele_right_click = self.driver.find_element_by_xpath('//input[@value="right click me"]')

        # actions = ActionChains(self.driver)
        # actions.click(ele_click)
        # actions.double_click(ele_double_click)
        # actions.context_click(ele_right_click)

        # actions.perform()
        ActionChains(self.driver).click(ele_click).double_click(ele_double_click).context_click(ele_right_click).perform()
        sleep(3)

    @pytest.mark.skip
    def test_moveelement(self):
        self.driver.get("https://www.baidu.com/")
        ele_settings = self.driver.find_element_by_id('s-usersetting-top')
        actions = ActionChains(self.driver)
        actions.move_to_element(ele_settings)
        actions.perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        ele_drag = self.driver.find_element_by_id('dragger')
        ele_drop = self.driver.find_element_by_xpath('//body/div[2]')

        actions = ActionChains(self.driver)
        # actions.drag_and_drop(ele_drag, ele_drop).perform()

        # actions.click_and_hold(ele_drag).release(ele_drop).perform()
        actions.click_and_hold(ele_drag).move_to_element(ele_drop).release().perform()
        sleep(3)

    @pytest.mark.skip
    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        self.driver.find_elements_by_xpath('//input[@type="textbox"]')[0].click()
        # self.driver.find_elements_by_xpath('//input[@type="textbox"]')[0].send_keys("username")
        # self.driver.find_elements_by_xpath('//input[@type="textbox"]')[0].send_keys(Keys.SPACE)
        # self.driver.find_elements_by_xpath('//input[@type="textbox"]')[0].send_keys("Tom")
        # self.driver.find_elements_by_xpath('//input[@type="textbox"]')[0].send_keys(Keys.BACK_SPACE)

        actions = ActionChains(self.driver)
        actions.send_keys("username").pause(1)
        actions.send_keys(Keys.SPACE).pause(1)
        actions.send_keys("tom").pause(1)
        actions.send_keys(Keys.BACK_SPACE).pause(1).perform()
        sleep(3)

    @pytest.mark.skip
    def test_touchaction_scroll(self):
        self.driver.get("https://www.baidu.com/")
        el = self.driver.find_element_by_id('kw')
        el_search = self.driver.find_element_by_id('su')
        actions = TouchActions(self.driver)
        el.send_keys("appium")
        actions.tap(el_search)
        actions.perform()
        actions.scroll_from_element(el, 0, 10000).perform()
        # sleep(3)

    @pytest.mark.skip
    def test_switch_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)

        self.driver.switch_to_window(self.driver.window_handles[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys("username")
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('phone')
        self.driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('phone')
        sleep(3)
        self.driver.switch_to_window(self.driver.window_handles[0])

        # sleep(1000)
        # self.driver.find_element_by_link_text("用户名登录").click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys("username")
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys("password")
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(3)

    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame("iframeResult")
        draggable = self.driver.find_element_by_id('draggable')
        droppable = self.driver.find_element_by_id('droppable')

        actions = ActionChains(self.driver)
        actions.drag_and_drop(draggable, droppable).perform()

        sleep(3)
        self.driver.switch_to_alert().accept()

        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_id('submitBTN').click()
        sleep(3)
        # self.driver.switch_to.default_content()

        # print(self.driver.find_element_by_id('draggable').text)
        # self.driver.switch_to.parent_frame()
        # print(self.driver.find_element_by_id('submitBTN').text)
        # sleep(3)

    def test_js(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, 'kw').send_keys("appium")
        element = self.driver.execute_script('return document.getElementById("su")')
        element.click()
        self.driver.execute_script('document.documentElement.scrollTop=1000')
        sleep(3)
        # self.driver.find_element_by_xpath("//*[@id='page']//a[10]").click()
        self.driver.find_element_by_xpath("//*[@id='page']//a[last()]").click()
        sleep(3)
        self.driver.execute_script('document.documentElement.scrollTop=1000')
        sleep(3)

        for code in ['return document.title', 'return JSON.stringify(performance.timing)']:
            print(self.driver.execute_script(code))

    def test_change_date(self):
        self.driver.get('https://www.12306.cn/index/')
        # self.driver.execute_script('document.getElementById("train_date").removeAttribute("readonly")')
        self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute("readonly")')
        sleep(3)
        self.driver.execute_script('document.getElementById("train_date").value="2020-12-30"')
        sleep(3)

    def test_upload_picture(self):
        self.driver.get('https://image.baidu.com/')
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        sleep(3)
        self.driver.find_element_by_id('stfile').send_keys('D:\\PycharmProjects\\SeleniumTest\\web\\resource\\80_80.png')
        sleep(3)


    # 跳过扫码登录（调试运行或者cookie注入）
    def test_wework(self):
        # self.driver.find_element_by_id('menu_contacts').click()
        # sleep(3)

        self.driver.get('https://work.weixin.qq.com/')
        # 创建或打开一个数据库
        db = shelve.open("cookies")
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1595836517'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853220984739'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325091155963'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'SrN66FlX3PbFDvmRh1EI0WAM11fyeh2FltvBB8ZA8btuYsNEH_oKukX3hGH9FYOe'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'Hm2Ds7Q3WiGy3D7qw1XZgwPXaHGUrMwFOHuKILj4HgfdTxB8NDJxKWxAqHzRkfcOJ73thtMEfiB3MECKMPr5ORYOPkDdlWb5_UXnOOSPARyGAAfOvAlsV3EfLmAS7049KIBTxSTy8h4C9UvqSbWL0cIU4ubkUMbKh7u_pYr_m5AnkKRUtINPIvdcqNKIRjd3XCUGIxozSGSPpG8gt63XvPS2sZdxPb76KcVTTbl2SL7taCgKB29qNRfUwYTNcEDKZRBC8Yrrq1ragv0VnqbWtA'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '643790848'}, {'domain': 'work.weixin.qq.com', 'expiry': 1595867120, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '4uogurj'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853220984739'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '40e6bd2adb1990558177554c7614d2d63dfc0a580c50282b7a35d22a68625b38'}, {'domain': '.work.weixin.qq.com', 'expiry': 1595867120, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1595922921, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.2054318020.1595835594'}, {'domain': '.work.weixin.qq.com', 'expiry': 1598428537, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.work.weixin.qq.com', 'expiry': 1627372517, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1595835620,1595836510,1595836517'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a1268560'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '7204234252384120'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'u3Jw8rEMW9'}, {'domain': '.qq.com', 'expiry': 1658908521, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.349151564.1592991994'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '6652736815'}]
        # 将数据存储到shelve数据库
        # db["cookies"] = cookies
        # 取出数据
        cookies = db['cookies']
        db.close()
        # 获取cookies
        # print(self.driver.get_cookies())

        # 把字典加入到driver的cookie中
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')

            self.driver.add_cookie(cookie)

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element_by_id('menu_contacts').click()
        sleep(3)


