#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:Fillico
# date:2019/6/23
# description:投标页面的测试用例
import logging
import time
import unittest

import pytest
from ddt import ddt, data
from selenium import webdriver
from PageObject.index_page import IndexPage
from PageObject.login_page import LoginPage
from PageObject.user_page import UserPage
from TestDatas import common_datas as CD
from TestDatas import invest_datas as ID
from TestDatas import login_datas as LD

from PageObject.bid_page import BidPage


def test_demo():
    print("类之外的测试用例")

@ddt
class TestInvestPage:

    @classmethod
    def setUpClass(cls):
        logging.info("======用例前置：初始化浏览器会话，登录前程贷系统======")
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(CD.web_login_url)
        # LoginPage(cls.driver).login(LD.success_data["user"], LD.success_data["password"])
        LoginPage(cls.driver).login(LD.success_data["user"], LD.success_data["password"])
        # 调用首页的一个函数,实现从首页任意选择一个标,点击抢投标按钮
        IndexPage(cls.driver).click_invest_btn()
        cls.bid_page = BidPage(cls.driver)
        # cls.user_page = UserPage(cls.driver)
        # 登录

    def tearDown(self):
        logging.info("======每一个用例后置：刷新当前页面======")
        self.driver.refresh()
        time.sleep(0.5)

    @classmethod
    def tearDownClass(cls):
        logging.info("======用例后置类：关闭浏览器会话，清理环境======")
        cls.driver.quit()

    @data(*ID.invest_fail_data)
    def test_invest_failed(self, data):
        logging.info("======投资用例：异常场景-投资金额为非100的整数倍======")
        # userMoney_beforeInvest = self.user_page.get_user_left_money()  # 投资前获取余额
        userMoney_beforeInvest = self.bid_page.get_user_left_money()  # 投资前获取余额
        self.bid_page.invest(data["invest_money"])  # 投资
        userMoney_afterInvest = self.bid_page.get_user_left_money()  # 投资后获取余额
        # 断言:投资前和投资后的金额是否相等
        self.assertEqual(userMoney_beforeInvest, userMoney_afterInvest)
        # 投资失败的弹出框文字
        self.assertEqual(self.bid_page.get_fail_alert_text(), data["check"])

    @data(*ID.invest_wrong_formater)
    def test_invest_failed_wrong_format(self, data):
        logging.info("======投资用例：异常场景-投资金额为错误的格式等======")
        # before_invest = self.bid_page.get_user_left_money()

        # self.bid_page.invest(data["invest_money"])
        btn_msg = self.bid_page.get_btn_text(data["invest_money"])
        # self.bid_page.get_element_text()
        # after_invest = self.user_page.get_user_left_money()
        # self.assertEqual(before_invest, after_invest)
        # 投资金额不是10的倍数,校验按钮上面的文字
        self.assertEqual(data["check"], btn_msg)

    @pytest.mark.smoke
    def test_invest_success(self):
        logging.info("======投资用例：正常场景-投资成功")
        before_invest = self.bid_page.get_user_left_money()
        self.bid_page.invest(ID.invest_success_data["invest_money"])
        self.bid_page.click_activeButton_on_success_popup()  # 点击查看并激活按钮
        # 投资成功,校验投资后的金额等于投资前的金额减去投资金额
        # self.assertEqual(int(float(UserPage(self.driver).get_user_left_money())),
        #                  (int(before_invest) - ID.invest_success_data["invest_money"]))
        self.assertEqual(ID.invest_success_data["invest_money"] , int(int(before_invest)-float(UserPage(self.driver).get_user_left_money())))
