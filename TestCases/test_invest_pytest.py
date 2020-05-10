#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:Fillico
# date:2019/6/30
# description:投标页面的测试用例


import logging
import time
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

@pytest.mark.usefixtures("login_web")  # 使用函数名称为login_web的fixture
@pytest.mark.usefixtures("refresh_page")
class TestInvestPage:

    pytestmark = pytest.mark.invest

    @pytest.mark.parametrize("data",ID.invest_fail_data)
    def test_invest_failed(self, data,login_web):
        logging.info("======投资用例：异常场景-投资金额为非100的整数倍======")
        userMoney_beforeInvest = BidPage(login_web).get_user_left_money()  # 投资前获取余额
        BidPage(login_web).invest(data["invest_money"])  # 投资
        userMoney_afterInvest = BidPage(login_web).get_user_left_money()  # 投资后获取余额
        # 断言:投资前和投资后的金额是否相等
        assert userMoney_beforeInvest == userMoney_afterInvest
        # 投资失败的弹出框文字
        assert BidPage(login_web).get_fail_alert_text() == data["check"]

    @pytest.mark.parametrize("data",ID.invest_wrong_formater)
    def test_invest_failed_wrong_format(self, data,login_web):
        logging.info("======投资用例：异常场景-投资金额为错误的格式等======")
        btn_msg = BidPage(login_web).get_btn_text(data["invest_money"])
        # 投资金额不是10的倍数,校验按钮上面的文字
        assert data["check"]== btn_msg

    @pytest.mark.smoke
    def test_invest_success(self,login_web):
        logging.info("======投资用例：正常场景-投资成功")
        before_invest = BidPage(login_web).get_user_left_money()
        BidPage(login_web).invest(ID.invest_success_data["invest_money"])
        BidPage(login_web).click_activeButton_on_success_popup()  # 点击查看并激活按钮
        # 投资成功,校验投资后的金额等于投资前的金额减去投资金额
        assert ID.invest_success_data["invest_money"] == int(int(before_invest)-float(UserPage(self.driver).get_user_left_money()))
