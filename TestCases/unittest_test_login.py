#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:Fillico
# date:2019/6/8
# function:登录页面的测试用例

import unittest

import pytest
from ddt import ddt, data
from selenium import webdriver
from PageObject.index_page import IndexPage
from PageObject.login_page import LoginPage
from TestDatas import login_datas as ld

from TestDatas import common_datas as cd


@ddt
@pytest.mark.login  # 整个TestLogin类里面，所有测试用例都有login标签
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 前置 - 打开网页，启动浏览器
        cls.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(30)
        cls.driver.get('{}/Index/login.html'.format(cd.base_url))
        cls.driver.maximize_window()  # 窗口最大化

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # 关闭浏览器

    def tearDown(self):
        self.driver.refresh()  # 刷新当前页面

    # 异常用例 - 读取test_cases里面的wrong_datas
    @data(*ld.wrong_datas)
    def test_login_0_failed_by_wrong_datas(self, data):  # 手机号为空
        LoginPage(self.driver).login(data["user"], data["password"])
        self.assertEqual(data["check"], LoginPage(self.driver).get_error_msg_from_loginForm())

    @data(*ld.fail_datas)
    def test_login_1_failed_by_fail_datas(self, data):
        LoginPage(self.driver).login(data["user"], data["password"])
        self.assertEqual(data["check"], LoginPage(self.driver).get_error_msg_from_pageCenter())

    # 正常用例：登录+首页，断言-页面是否存在 “关于我们” 元素
    @pytest.mark.smoke
    def test_login_2_success(self):
        LoginPage(self.driver).login(ld.success_data["user"], ld.success_data["password"])
        self.assertTrue(IndexPage(self.driver).check_nick_name_exists())
        # url跳转，比对当前的url结果和实际结果
        self.assertEqual(self.driver.current_url, ld.success_data["check"])


        # def test_login_failed_by_no_username(self, data):  # 手机号为空
        #     LoginPage(self.driver).login('','python' )
        #     print(LoginPage(self.driver).get_error_msg_from_loginForm())
        #     self.assertEqual('请输入手机号', LoginPage(self.driver).get_error_msg_from_loginForm())
        #     # self.assertEqual(self.driver.find_element_by_xpath('//input[@name="password"]/following-sibling::div').text,
        #     # '请输入密码')


        # # 异常用例 - 输入正确的手机号，密码为空
        # def test_login_failed_by_no_pwd(self):
        #     LoginPage(self.driver).login('18684720553', '')
        #     print(LoginPage(self.driver).get_error_msg_from_loginForm())
        #     self.assertEqual('请输入密码', LoginPage(self.driver).get_error_msg_from_loginForm())
        #
        #
        # # 输入正确的手机号，错误的密码
        # def test_login_failed_by_wrong_pwd(self):
        #     LoginPage(self.driver).login('18684720553', '123456')
        #     # WebDriverWait(self.driver, 20).until(
        #     #     EC.visibility_of_element_located((By.XPATH, '//div[@class="layui-layer-content"]')))
        #     # print(self.driver.find_element_by_xpath('//div[@class="layui-layer-content"]').text)
        #     print(LoginPage(self.driver).get_error_msg_from_loginForm())
        #     self.assertEqual('帐号或密码错误!', LoginPage(self.driver).get_error_msg_from_loginForm())
        #
        #
        # # 输入没有注册过的手机号，一个正确的密码
        # def test_login_failed_by_no_register(self):
        #     LoginPage(self.driver).login('13200000000', 'python')
        #     # WebDriverWait(self.driver, 20).until(
        #     #     EC.visibility_of_element_located((By.XPATH, '//div[@class="layui-layer-content"]')))
        #     print(LoginPage(self.driver).get_error_msg_from_pageCenter())
        #     self.assertEqual('此账号没有经过授权，请联系管理员!',
        #                      LoginPage(self.driver).get_error_msg_from_pageCenter())
        #
        #
        # # 手机输入12位，一个正确的密码
        # def test_login_fail_more_numb(self):
        #     LoginPage(self.driver).login('186847205531', 'python')
        #     print(LoginPage(self.driver).get_error_msg_from_loginForm())
        #     self.assertEqual('请输入正确的手机号', LoginPage(self.driver).get_error_msg_from_loginForm())
        #
        #
        # # 手机输入12位，一个正确的密码
        # def test_login_fail_less_numb(self):
        #     LoginPage(self.driver).login('18684720553', 'python')
        #     print(LoginPage(self.driver).get_error_msg_from_loginForm())
        #     self.assertEqual('请输入正确的手机号', LoginPage(self.driver).get_error_msg_from_loginForm())
        #
        #
        # # 手机输入正确的手机号，手机号末尾有空格，一个正确的密码
        # def test_login_success_contains_space(self):
        #     LoginPage(self.driver).login('18684720553 ', 'python')
        #     print(LoginPage(self.driver).get_error_msg_from_loginForm())
        #     self.assertTrue(IndexPage(self.driver).check_nick_name_exists())
        #     self.assertEqual(self.driver.current_url, 'http://120.78.128.25:8765/Index/index')
        #
        #
        # # 手机输入正确的手机号，手机号中间有空格，一个正确的密码
        # def test_login_failed_by_space(self):
        #     LoginPage(self.driver).login('1868472 0553', 'python')
        #     print(LoginPage(self.driver).get_error_msg_from_loginForm())
        #     self.assertEqual(LoginPage(self.driver).get_error_msg_from_loginForm(),
        #                      '请输入正确的手机号')
        #
        #
        # # 手机号输入11位，中间包含非数字字符，一个正确的密码
        # def test_login_fail_by_special_character(self):
        #     LoginPage(self.driver).login('186847aa553', 'python')
        #     print(LoginPage(self.driver).get_error_msg_from_loginForm())
        #     self.assertEqual(LoginPage(self.driver).get_error_msg_from_loginForm(),
        #                      '请输入正确的手机号')
