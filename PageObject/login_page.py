#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:Fillico
# date:2019/6/7
# function:

from Common.basepage import BasePage

from PageLocators.login_page_locator import LoginPageLocator as loc


class LoginPage(BasePage):

    # 登录功能
    def login(self, username, password):
        self.input_text(loc.user_loc,"登录页面_用户名输入框",username)
        self.input_text(loc.passwd_loc,"登录页面_密码输入框",password)
        self.click_element(loc.login_button_loc,"登录页面_登录按钮")  # 点击登录按钮

    # 异常场景 - 获取表单区域的错误信息
    def get_error_msg_from_loginForm(self):
        return self.get_element_text(loc.error_msg_from_loginForm,"登录页面_表单区域错误信息")
        # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.error_msg_from_loginForm))
        # return self.driver.find_element(*loc.error_msg_from_loginForm).text

    # 获取页面中间的错误信息
    def get_error_msg_from_pageCenter(self):
        # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.error_notify_from_pageCenter))
        # return self.driver.find_element(*loc.error_notify_from_pageCenter).text
        self.wait_eleVisible(loc.error_notify_from_pageCenter,"登录页面_页面中间的错误信息")
        return self.get_element_text(loc.error_notify_from_pageCenter,"登录页面_页面中间的错误信息")