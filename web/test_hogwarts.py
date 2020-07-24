import os
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